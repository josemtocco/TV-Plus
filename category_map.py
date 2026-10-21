# Category normalization map: lowercase key -> canonical name
# Também usa matching parcial / contains e prioridade por nome do canal

CATEGORY_SYNONYMS = {
    # Notícias / News
    "noticias": "Notícias",
    "notícias": "Notícias",
    "news": "Notícias",
    "noticia": "Notícias",
    "notícia": "Notícias",
    "jornalismo": "Notícias",
    "jornal": "Notícias",
    "globonews": "Notícias",
    "globo news": "Notícias",

    # Desenhos / Kids / Infantil
    "desenhos": "Infantil",
    "desenho": "Infantil",
    "kids": "Infantil",
    "infantil": "Infantil",
    "criança": "Infantil",
    "criancas": "Infantil",
    "crianças": "Infantil",
    "child": "Infantil",
    "children": "Infantil",
    "cartoon": "Infantil",
    "cartoons": "Infantil",
    "animacao": "Infantil",
    "animação": "Infantil",
    "animes": "Infantil",
    "anime": "Infantil",
    "animation": "Infantil",

    # Cinema / Filmes
    "cinema": "Filmes",
    "filmes": "Filmes",
    "filme": "Filmes",
    "movies": "Filmes",
    "movie": "Filmes",
    "classicos": "Filmes",
    "clássicos": "Filmes",
    "classico": "Filmes",
    "clássico": "Filmes",
    "classic": "Filmes",
    "faroeste": "Filmes",
    "western": "Filmes",

    # Esportes
    "esportes": "Esportes",
    "esporte": "Esportes",
    "sports": "Esportes",
    "sport": "Esportes",
    "futebol": "Esportes",
    "football": "Esportes",
    "games": "Esportes",

    # Música
    "musicas": "Música",
    "músicas": "Música",
    "musica": "Música",
    "música": "Música",
    "music": "Música",
    "videoclipes": "Música",
    "clipes": "Música",
    "radio": "Música",
    "rádio": "Música",
    "radios": "Música",
    "rádios": "Música",
    "flashback": "Música",
    "pop": "Música",

    # Seriados / Séries
    "seriados": "Séries",
    "series": "Séries",
    "séries": "Séries",
    "serie": "Séries",
    "série": "Séries",
    "novelas": "Séries",
    "novela": "Séries",

    # Variedades
    "variedades": "Variedades",
    "variedade": "Variedades",
    "entretenimento": "Variedades",
    "entertainment": "Variedades",
    "geral": "Variedades",
    "general": "Variedades",
    "eclética": "Variedades",
    "ecletica": "Variedades",
    "lifestyle": "Variedades",
    "jovem": "Variedades",
    "comedy": "Variedades",
    "reality": "Variedades",

    # TVs Abertas / Canais Abertos
    "tvs abertas": "TVs Abertas",
    "tv aberta": "TVs Abertas",
    "canais abertos": "TVs Abertas",
    "abertos": "TVs Abertas",
    "aberta": "TVs Abertas",
    "publicos": "TVs Abertas",
    "públicos": "TVs Abertas",
    "publico": "TVs Abertas",
    "público": "TVs Abertas",
    "tv brasil": "TVs Abertas",
    "tv": "TVs Abertas",
    "rede nbx tv": "TVs Abertas",
    "rede nbx": "TVs Abertas",
    "regionais": "TVs Abertas",
    "regional": "TVs Abertas",
    "comunitaria": "TVs Abertas",
    "comunitária": "TVs Abertas",
    "retransmissora": "TVs Abertas",
    "governo": "TVs Abertas",
    "legislative": "TVs Abertas",
    # Alta Definição → realocada para TVs Abertas (sem categoria própria)
    "alta definição": "TVs Abertas",
    "alta definicao": "TVs Abertas",
    "alta definição ( hd,fhd )": "TVs Abertas",
    "hd": "TVs Abertas",
    "fhd": "TVs Abertas",

    # Documentários (inclui ex-Animais / Pet)
    "documentarios": "Documentários",
    "documentários": "Documentários",
    "documentario": "Documentários",
    "documentário": "Documentários",
    "docs": "Documentários",
    "documentary": "Documentários",
    "animais": "Documentários",
    "animal": "Documentários",
    "pet": "Documentários",

    # Religiosos
    "evangelicos": "Religiosos",
    "evangélicos": "Religiosos",
    "evangelico": "Religiosos",
    "evangélico": "Religiosos",
    "evangelica": "Religiosos",
    "evangélica": "Religiosos",
    "gospel": "Religiosos",
    "catolicos": "Religiosos",
    "católicos": "Religiosos",
    "catolico": "Religiosos",
    "católico": "Religiosos",
    "catolica": "Religiosos",
    "católica": "Religiosos",
    "religioso": "Religiosos",
    "religiosos": "Religiosos",
    "religious": "Religiosos",
    "igreja": "Religiosos",

    # Culinária
    "culinarias": "Culinária",
    "culinárias": "Culinária",
    "culinaria": "Culinária",
    "culinária": "Culinária",
    "comida": "Culinária",
    "cooking": "Culinária",
    "gastronomia": "Culinária",

    # Educativos + Cultura (unificados)
    "educativos": "Educativos / Cultura",
    "educativo": "Educativos / Cultura",
    "educacao": "Educativos / Cultura",
    "educação": "Educativos / Cultura",
    "education": "Educativos / Cultura",
    "educativa": "Educativos / Cultura",
    "cultura": "Educativos / Cultura",
    "cultural": "Educativos / Cultura",
    "culture": "Educativos / Cultura",

    # Automóveis
    "automoveis": "Automóveis",
    "automóveis": "Automóveis",
    "automovel": "Automóveis",
    "automóvel": "Automóveis",
    "carros": "Automóveis",
    "carro": "Automóveis",
    "auto": "Automóveis",

    # Televendas
    "televendas": "Televendas",
    "vendas": "Televendas",
    "shopping": "Televendas",

    # Agronegócio
    "agronegocio": "Agronegócio",
    "agronegócio": "Agronegócio",
    "agronegocios": "Agronegócio",
    "agronegócios": "Agronegócio",
    "agro": "Agronegócio",
    "rural": "Agronegócio",
    "campo": "Agronegócio",

    # Internacional
    "internacional": "Internacional",
    "international": "Internacional",

    # Plataformas dedicadas (também por group se vier)
    "pluto tv": "Pluto Tv",
    "pluto": "Pluto Tv",
    "hallo tv": "Hallo Tv",
    "hallo": "Hallo Tv",
    "urban tv": "Urban TV",
    "urban": "Urban TV",
    "web tv": "Web TV",
    "webtv": "Web TV",

    # Outros
    "sem categoria": "Outros",
    "outros": "Outros",
    "other": "Outros",
    "undefined": "Outros",
    "brazil": "TVs Abertas",
    "brasil": "TVs Abertas",

    "sp": "TVs Abertas",
    "posição premium": "Variedades",
    "posicao premium": "Variedades",
    "minas": "TVs Abertas",
    "outdoor": "Variedades",
    "travel": "Variedades",
    "family": "Variedades",
    "câmera": "Variedades",
    "camera": "Variedades",
    "pop rock": "Música",
    "popular": "Música",
    "ceara": "TVs Abertas",
    "ceará": "TVs Abertas",
    "estudio fm": "Música",
    "para": "TVs Abertas",
    "rn": "TVs Abertas",
    "étnicos": "Internacional",
    "etnicos": "Internacional",
}

# Keywords that if present in the raw group (after lower) map to category
CONTAINS_MAP = [
    ("notícia", "Notícias"),
    ("noticia", "Notícias"),
    ("news", "Notícias"),
    ("jornal", "Notícias"),
    ("globo news", "Notícias"),
    ("globonews", "Notícias"),
    ("desenho", "Infantil"),
    ("kids", "Infantil"),
    ("infantil", "Infantil"),
    ("criança", "Infantil"),
    ("anime", "Infantil"),
    ("animation", "Infantil"),
    ("filme", "Filmes"),
    ("cinema", "Filmes"),
    ("movie", "Filmes"),
    ("classic", "Filmes"),
    ("esporte", "Esportes"),
    ("sport", "Esportes"),
    ("futebol", "Esportes"),
    ("game", "Esportes"),
    ("música", "Música"),
    ("musica", "Música"),
    ("music", "Música"),
    ("rádio", "Música"),
    ("radio", "Música"),
    ("série", "Séries"),
    ("serie", "Séries"),
    ("novela", "Séries"),
    ("variedad", "Variedades"),
    ("entertainment", "Variedades"),
    ("documentár", "Documentários"),
    ("documentar", "Documentários"),
    ("documentary", "Documentários"),
    ("animal", "Documentários"),   # ex-Animais → Documentários
    ("pet", "Documentários"),
    ("evangélic", "Religiosos"),
    ("evangelic", "Religiosos"),
    ("gospel", "Religiosos"),
    ("católic", "Religiosos"),
    ("catolic", "Religiosos"),
    ("religio", "Religiosos"),
    ("culinár", "Culinária"),
    ("culinari", "Culinária"),
    ("cooking", "Culinária"),
    ("educativ", "Educativos / Cultura"),
    ("educaç", "Educativos / Cultura"),
    ("education", "Educativos / Cultura"),
    ("cultur", "Educativos / Cultura"),
    ("automó", "Automóveis"),
    ("automov", "Automóveis"),
    ("carro", "Automóveis"),
    ("televenda", "Televendas"),
    ("agro", "Agronegócio"),
    ("rural", "Agronegócio"),
    ("abert", "TVs Abertas"),
    ("regional", "TVs Abertas"),
    ("alta def", "TVs Abertas"),
    ("internacional", "Internacional"),
    ("pluto", "Pluto Tv"),
    ("hallo", "Hallo Tv"),
    ("urban", "Urban TV"),
    ("web tv", "Web TV"),
    ("webtv", "Web TV"),
    ("premium", "Variedades"),
    ("outdoor", "Variedades"),
    ("travel", "Variedades"),
    ("family", "Variedades"),
    ("câmera", "Variedades"),
    ("camera", "Variedades"),
    ("pop rock", "Música"),
    ("étnic", "Internacional"),
    ("etnic", "Internacional"),
    ("fm", "Música"),
]


def normalize_category(raw: str, channel_name: str = "") -> str:
    """
    Normaliza a categoria.
    Prioridade:
      1. Nome do canal (plataformas Pluto / Hallo / Urban / Web TV e GloboNews)
      2. group-title exato / contains
    """
    name_lower = (channel_name or "").strip().lower()
    original = (raw or "").strip()
    key = original.lower()

    # --- Prioridade 1: nome do canal (plataformas e casos especiais) ---
    if name_lower:
        if "pluto" in name_lower:
            return "Pluto Tv"
        # Hallo TV (evita falso positivo de Halloween)
        if "hallo" in name_lower and "halloween" not in name_lower:
            return "Hallo Tv"
        if "urban" in name_lower or "trace urban" in name_lower:
            return "Urban TV"
        if "web tv" in name_lower or "webtv" in name_lower or "web-tv" in name_lower:
            return "Web TV"
        if "globonews" in name_lower or "globo news" in name_lower:
            return "Notícias"

    # --- Prioridade 2: group-title ---
    if not original:
        return "Outros"

    # Exact match
    if key in CATEGORY_SYNONYMS:
        return CATEGORY_SYNONYMS[key]

    # Contains / partial
    for fragment, cat in CONTAINS_MAP:
        if fragment in key:
            return cat

    # Evitar categorias longas ou estranhas
    if len(original) > 40 or ";" in original or "/" in original:
        return "Outros"

    return original.title() if original else "Outros"
