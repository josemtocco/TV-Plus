import re
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
    "infantis": "Infantil",
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

    # TV / Canais Abertos
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
    # Alta Definição → realocada para TV (sem categoria própria)
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

    # Automóveis → Esportes (unificado)
    "automoveis": "Esportes",
    "automóveis": "Esportes",
    "automovel": "Esportes",
    "automóvel": "Esportes",
    "carros": "Esportes",
    "carro": "Esportes",
    "auto": "Esportes",

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
    "runtime tv": "Runtime TV",
    "runtime.tv": "Runtime TV",
    "runtime": "Runtime TV",

    # Outros
    "sem categoria": "Outros",
    "outros": "Outros",
    "rs": "RS",
    "rio grande do sul": "RS",
    "other": "Outros",
    "undefined": "Outros",
    "brazil": "TVs Abertas",
    "brasil": "TVs Abertas",

    "sp": "TVs Abertas",
    "posição premium": "Variedades",
    "posicao premium": "Variedades",
    "minas": "TVs Abertas",
    "outdoor": "Variedades",
    "travel": "Documentários",
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
    "natureza": "Documentários",
    "viagem": "Documentários",
    "weather": "Documentários",
    "wild": "Documentários",
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
    ("infantis", "Infantil"),
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
    ("automó", "Esportes"),
    ("automov", "Esportes"),
    ("carro", "Esportes"),
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
    ("runtime", "Runtime TV"),
    ("premium", "Variedades"),
    ("outdoor", "Variedades"),
    ("travel", "Documentários"),
    ("natureza", "Documentários"),
    ("viagem", "Documentários"),
    ("weather", "Documentários"),
    ("wild", "Documentários"),
    ("family", "Variedades"),
    ("câmera", "Variedades"),
    ("camera", "Variedades"),
    ("pop rock", "Música"),
    ("étnic", "Internacional"),
    ("etnic", "Internacional"),
    ("fm", "Música"),
]


# Palavras no nome do canal → Documentários
DOC_NAME_KEYWORDS = [
    "nature time",
    "nature love",
    "natureza",
    "animais",
    "travel",
    "doc",
    "viagem",
    "weather",
    "wild",
]

# Palavras no nome do canal → Notícias
NEWS_NAME_KEYWORDS = [
    "band news",
    "jovem pan news",
    "record news",
    "canal uol",
    "veja +",
    "veja+",
    "a critica",
    "a crítica",
    "sbt news",
    "times brasil cnbc",
    "caras tv",
    "new brasil",
    "news",
    "cnn",
]

# Esportes por nome do canal
SPORTS_NAME_KEYWORDS = [
    "sports",
    "espn",
    "sporttv",
    "sport tv",
    "motors",
    "motor",
    "fifa",
    "ge tv",
    "caze tv",
    "cazé tv",
    "canal goat",
    "goat",
]

# Filmes por nome do canal
FILMES_NAME_KEYWORDS = [
    "cinema em casa",
    "bora",
    "entretendo",
    "adrenalina pura",
    "filmelier",
    "filmrise",
    "soplaymovies",
    "soplay movies",
]

# Infantil por nome
INFANTIL_NAME_KEYWORDS = [
    "dpa fast",
    "d.p.a",
    "dpa",
]


# Frases/palavras no nome → categoria NOVA "TV" (redes principais)
TV_NAME_PHRASES = [
    "rede globo",
    "globo tv",
    "tv brasil",
    "tv cultura",
    "rede tv",
    "tv pampa",
    "rede tv!",
    "catve",
    "rede brasil",
]
TV_NAME_WORDS = [
    "globo",
    "sbt",
    "band",
    "record",
    "tve",
    "bandeirantes",
    "ngt",
]

# Categoria RS (Rio Grande do Sul) — palavras e cidades
RS_NAME_PHRASES = [
    "porto alegre",
    "passo fundo",
    "santa maria",
    "conecta mais tv",
    "conecta mais",
    "lagoatv",
    "lagoa tv",
    "studio tv",
    "caxias do sul",
    "novo hamburgo",
    "sao leopoldo",
    "são leopoldo",
    "rio grande",
    "bento goncalves",
    "bento gonçalves",
    "santana do livramento",
    "uruguaiana",
    "cruz alta",
    "vacaria",
    "lajeado",
    "gramado",
    "canela",
    "osorio",
    "osório",
    "torres",
    "sapucaia",
    "esteio",
    "sapiranga",
    "farroupilha",
    "erechim",
    "pelotas",
    "canoas",
    "gravatai",
    "gravataí",
    "viamao",
    "viamão",
    "alvorada",
    "cachoeirinha",
    "bage",
    "bagé",
    "santa cruz do sul",
    "sao borja",
    "são borja",
]
RS_NAME_WORDS = [
    "poa",
    "adesso",
    "serrana",
    "gaucha",
    "gaúcha",
    "gaucho",
    "gaúcho",
    "ijui",
    "ijuí",
    "mon",  # marca local; limite de palavra
]

def normalize_category(raw: str, channel_name: str = "") -> str:
    """
    Normaliza a categoria.
    Prioridade:
      1. Nome do canal (plataformas, Documentários, Música, Notícias, Esportes, RS, TV)
      2. group-title exato / contains
    """
    name_lower = (channel_name or "").strip().lower()
    original = (raw or "").strip()
    key = original.lower()

    # --- Prioridade 1: nome do canal ---
    if name_lower:
        # Plataformas dedicadas
        if "pluto" in name_lower:
            return "Pluto Tv"
        if "hallo" in name_lower and "halloween" not in name_lower:
            return "Hallo Tv"
        if "urban" in name_lower or "trace urban" in name_lower:
            return "Urban TV"
        if "web tv" in name_lower or "webtv" in name_lower or "web-tv" in name_lower:
            return "Web TV"
        if "runtime" in name_lower:
            return "Runtime TV"

        # Documentários
        for kw in DOC_NAME_KEYWORDS:
            if kw in name_lower:
                return "Documentários"

        # Infantil (ex.: DPA Fast)
        for kw in INFANTIL_NAME_KEYWORDS:
            if kw in name_lower:
                return "Infantil"

        # Filmes por nome
        for kw in FILMES_NAME_KEYWORDS:
            if kw in name_lower:
                return "Filmes"
        # "film" como palavra (Film, Film XYZ) — evita falsos amplos demais
        if re.search(r"\bfilm\b", name_lower) or "film " in name_lower or name_lower.startswith("film"):
            return "Filmes"

        # Música: começa com número, FM, radio/rádio
        name_stripped = name_lower.lstrip()
        if name_stripped and name_stripped[0].isdigit():
            return "Música"
        if "fm" in name_lower or "radio" in name_lower or "rádio" in name_lower:
            return "Música"

        # Notícias
        for kw in NEWS_NAME_KEYWORDS:
            if kw in name_lower:
                return "Notícias"

        # Esportes
        for kw in SPORTS_NAME_KEYWORDS:
            if kw in name_lower:
                return "Esportes"

        # RS (Rio Grande do Sul)
        for phrase in RS_NAME_PHRASES:
            if phrase in name_lower:
                return "RS"
        for word in RS_NAME_WORDS:
            if re.search(r"\b" + re.escape(word) + r"\b", name_lower):
                return "RS"

        # TV (redes principais)
        for phrase in TV_NAME_PHRASES:
            if phrase in name_lower:
                return "TV"
        for word in TV_NAME_WORDS:
            if re.search(r"\b" + re.escape(word) + r"\b", name_lower):
                return "TV"

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
