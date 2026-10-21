#!/usr/bin/env python3
"""
Gera lista M3U otimizada para SS IPTV a partir de múltiplas fontes.
- Deduplica por URL
- Normaliza categorias (case + sinônimos)
- Mantém canais que sumiram por até 3 atualizações
- Atualiza a cada 6h via GitHub Actions
"""

import json
import re
import os
import sys
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from collections import defaultdict
from category_map import normalize_category

SOURCES = [
    "https://raw.githubusercontent.com/josemtocco/-olhosnatv-brasil/refs/heads/main/olhosnatv.m3u",
    "https://raw.githubusercontent.com/josemtocco/ketv-m3u/refs/heads/main/ketv.m3u",
    "https://raw.githubusercontent.com/josemtocco/Paster/refs/heads/main/brasil.m3u",
    "https://raw.githubusercontent.com/josemtocco/clubecanais-m3u/refs/heads/main/clubecanais.m3u",
    "https://raw.githubusercontent.com/josemtocco/m3u-ssiptv-br/refs/heads/main/lista.m3u",
    "https://raw.githubusercontent.com/josemtocco/tvgarden-br-m3u/refs/heads/main/lista.m3u",
    "https://raw.githubusercontent.com/josemtocco/vidks_m3u/refs/heads/main/vidks.m3u",
    "https://raw.githubusercontent.com/josemtocco/batistaplay/refs/heads/main/batistaplay.m3u",
    "https://raw.githubusercontent.com/josemtocco/xttv-m3u-ssiptv/refs/heads/main/lista.m3u",
    "https://raw.githubusercontent.com/josemtocco/soultv_m3u/refs/heads/main/soultv.m3u",
    "https://raw.githubusercontent.com/josemtocco/iptv-br-updater/refs/heads/main/playlists/canais_br_todos.m3u",
    "https://raw.githubusercontent.com/josemtocco/iptvcat/refs/heads/main/brazil_ssiptv.m3u",
    "https://raw.githubusercontent.com/josemtocco/IPTV-BR/refs/heads/main/playlist.m3u",
    "https://raw.githubusercontent.com/josemtocco/brasil-tv-m3u-scr-v3/refs/heads/main/output/brasil-tv.m3u",
    "https://raw.githubusercontent.com/josemtocco/brasil-stream-catalog/refs/heads/main/canais.m3u",
    "https://raw.githubusercontent.com/josemtocco/tv-brasil-m3u/refs/heads/main/tv-brasil.m3u",
    "https://raw.githubusercontent.com/josemtocco/CanaisBR-brasil-tv-m3u-scr-v12-definitiva/refs/heads/main/output/brasil-tv.m3u",
    "https://raw.githubusercontent.com/josemtocco/mais-sbt-m3u/refs/heads/main/mais-sbt.m3u",
]

STATE_FILE = "state.json"
OUTPUT_M3U = "lista_ssiptv.m3u"
MAX_FAILS = 3
USER_AGENT = "Mozilla/5.0 (compatible; SSI PTV-Updater/1.0)"

# Ordem preferencial das categorias no M3U final
CATEGORY_ORDER = [
    "TVs Abertas",
    "Notícias",
    "Esportes",
    "Filmes",
    "Séries",
    "Infantil",
    "Música",
    "Documentários",
    "Variedades",
    "Religiosos",
    "Culinária",
    "Educativos / Cultura",
    "Pluto Tv",
    "Hallo Tv",
    "Urban TV",
    "Web TV",
    "Automóveis",
    "Agronegócio",
    "Televendas",
    "Internacional",
    "Outros",
]


def fetch_url(url: str, timeout: int = 30) -> str:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"[WARN] Falha ao baixar {url}: {e}", file=sys.stderr)
        return ""


def parse_m3u(content: str) -> list[dict]:
    """Parse M3U and return list of channel dicts."""
    channels = []
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#EXTINF:"):
            # Extract attributes
            info = line[8:]  # after #EXTINF:
            # duration,attrs,name
            comma = info.rfind(",")
            if comma == -1:
                i += 1
                continue
            attrs_part = info[:comma]
            name = info[comma + 1 :].strip()

            group = ""
            logo = ""
            tvg_id = ""
            tvg_name = ""

            # group-title=
            m = re.search(r'group-title="([^"]*)"', attrs_part, re.I)
            if m:
                group = m.group(1)
            m = re.search(r'tvg-logo="([^"]*)"', attrs_part, re.I)
            if m:
                logo = m.group(1)
            m = re.search(r'tvg-id="([^"]*)"', attrs_part, re.I)
            if m:
                tvg_id = m.group(1)
            m = re.search(r'tvg-name="([^"]*)"', attrs_part, re.I)
            if m:
                tvg_name = m.group(1)

            # next non-empty non-comment line is URL
            i += 1
            while i < len(lines):
                url_line = lines[i].strip()
                if url_line and not url_line.startswith("#"):
                    channels.append({
                        "name": name or tvg_name or "Sem Nome",
                        "url": url_line,
                        "group": group,
                        "logo": logo,
                        "tvg_id": tvg_id,
                        "tvg_name": tvg_name or name,
                    })
                    break
                i += 1
        i += 1
    return channels


def load_state() -> dict:
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[WARN] Erro ao carregar state: {e}", file=sys.stderr)
    return {"channels": {}, "last_update": None}


def save_state(state: dict):
    state["last_update"] = datetime.now(timezone.utc).isoformat()
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def merge_channels(current: dict[str, dict], previous: dict[str, dict]) -> dict[str, dict]:
    """
    current: url -> channel info (from sources now)
    previous: url -> {name, logo, group, fail_count, ...}
    Returns final dict of channels to keep.
    """
    result = {}
    # Process current ones
    for url, ch in current.items():
        prev = previous.get(url, {})
        result[url] = {
            "name": ch["name"],
            "logo": ch.get("logo") or prev.get("logo", ""),
            "group": normalize_category(ch["group"], ch.get("name", "")),
            "tvg_id": ch.get("tvg_id") or prev.get("tvg_id", ""),
            "tvg_name": ch.get("tvg_name") or prev.get("tvg_name", ch["name"]),
            "fail_count": 0,
            "last_seen": datetime.now(timezone.utc).isoformat(),
        }

    # Previous that are missing: increment fail
    for url, prev in previous.items():
        if url in result:
            continue
        fails = prev.get("fail_count", 0) + 1
        if fails < MAX_FAILS:
            result[url] = {
                "name": prev.get("name", "Sem Nome"),
                "logo": prev.get("logo", ""),
                "group": normalize_category(prev.get("group", "Outros"), prev.get("name", "")),
                "tvg_id": prev.get("tvg_id", ""),
                "tvg_name": prev.get("tvg_name", prev.get("name", "")),
                "fail_count": fails,
                "last_seen": prev.get("last_seen"),
            }
            print(f"[KEEP] {prev.get('name')} (falhas: {fails}/{MAX_FAILS})")
        else:
            print(f"[DROP] {prev.get('name')} (falhas >= {MAX_FAILS})")

    return result


def write_m3u(channels: dict[str, dict], path: str):
    # Group by normalized category
    by_cat = defaultdict(list)
    for url, ch in channels.items():
        cat = normalize_category(ch.get("group", ""), ch.get("name", ""))
        by_cat[cat].append((url, ch))

    # Sort categories
    ordered_cats = [c for c in CATEGORY_ORDER if c in by_cat]
    for c in sorted(by_cat.keys()):
        if c not in ordered_cats:
            ordered_cats.append(c)

    lines = [
        "#EXTM3U",
        f"#PLAYLIST: Lista BR Otimizada SS IPTV | Atualizada: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "#EXTSIZE: medium",  # default medium tiles for better visibility
    ]

    total = 0
    for cat in ordered_cats:
        items = by_cat[cat]
        # Sort by name
        items.sort(key=lambda x: x[1]["name"].lower())
        for url, ch in items:
            name = ch["name"]
            logo = ch.get("logo", "")
            tvg_id = ch.get("tvg_id", "")
            tvg_name = ch.get("tvg_name", name)

            attrs = f'-1 tvg-id="{tvg_id}" tvg-name="{tvg_name}"'
            if logo:
                attrs += f' tvg-logo="{logo}"'
            attrs += f' group-title="{cat}"'

            lines.append(f"#EXTINF:{attrs},{name}")
            lines.append("#EXTSIZE: medium")
            lines.append(url)
            total += 1

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"[OK] Gerado {path} com {total} canais em {len(ordered_cats)} categorias.")


def main():
    print(f"=== Atualizando lista SS IPTV @ {datetime.now(timezone.utc).isoformat()} ===")
    state = load_state()
    previous = state.get("channels", {})

    # Collect all current channels, dedupe by URL (last wins, or prefer longer name)
    current: dict[str, dict] = {}
    for src in SOURCES:
        print(f"Baixando: {src}")
        content = fetch_url(src)
        if not content:
            continue
        parsed = parse_m3u(content)
        print(f"  -> {len(parsed)} canais")
        for ch in parsed:
            url = ch["url"].strip()
            if not url or url.startswith("#"):
                continue
            # Normalize group early (usa nome do canal para plataformas Pluto/Hallo/Urban/Web TV etc.)
            ch["group"] = normalize_category(ch.get("group", ""), ch.get("name", ""))
            if url not in current or len(ch["name"]) > len(current[url]["name"]):
                current[url] = ch

    print(f"Total únicos das fontes: {len(current)}")

    final = merge_channels(current, previous)
    print(f"Total após merge (com persistência): {len(final)}")

    # Update state
    state["channels"] = final
    save_state(state)

    write_m3u(final, OUTPUT_M3U)

    # Summary by category
    from collections import Counter
    cats = Counter(normalize_category(ch.get("group", ""), ch.get("name", "")) for ch in final.values())
    print("\nCategorias:")
    for cat, cnt in cats.most_common():
        print(f"  {cat}: {cnt}")


if __name__ == "__main__":
    main()
