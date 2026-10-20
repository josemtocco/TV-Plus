# Category normalization map: lowercase key -> canonical name
# Também usa matching parcial / contains

CATEGORY_SYNONYMS = {
    # Hallo / Hallo
    "hallo": "Hallo",
    "hallotv": "Hallo",
    "hallo tv": "Hallo",

    # Pluto TV / Pluto TV
    "pluto": "Pluto TV",
    "plutotv": "Pluto TV",
    "pluto tv": "Pluto TV",
    
    # Urban TV / Urban TV
    "Urban": "Urban TV",
    "Urbantv": "Urban TV",
    "Urban tv": "Urban TV",

    # Runtime / Runtime TV
    "Runtime": "Runtime TV",
    "Runtimetv": "Runtime TV",
    "Runtime tv": "Runtime TV",

    # Notícias / News
    "noticias": "Notícias",
    "notícias": "Notícias",
    "news": "Notícias",
    "noticia": "Notícias",
    "notícia": "Notícias",
    "jornalismo": "Notícias",
    "jornal": "Notícias",
    
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
    "webtv": "TVs Abertas",
    "regionais": "TVs Abertas",
    "regional": "TVs Abertas",
    "comunitaria": "TVs Abertas",
    "comunitária": "TVs Abertas",
    "retransmissora": "TVs Abertas",
    "governo": "TVs Abertas",
    "legislative": "TVs Abertas",
    "alta definição": "TVs Abertas",
    "alta definicao": "TVs Abertas",
    "hd": "TVs Abertas",
    "fhd": "TVs Abertas",
    
    # Documentários
    "documentarios": "Documentários",
    "documentários": "Documentários",
    "documentario": "Documentários",
    "documentário": "Documentários",
    "docs": "Documentários",
    "documentary": "Documentários",
    
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
    
    # Educativos
    "educativos": "Educativos",
    "educativo": "Educativos",
    "educacao": "Educativos",
    "educação": "Educativos",
    "education": "Educativos",
    "educativa": "Educativos",
    
    # Cultura
    "cultura": "Cultura",
    "cultural": "Cultura",
    "culture": "Cultura",
    
    # Automóveis
    "automoveis": "Automóveis",
    "automóveis": "Automóveis",
    "automovel": "Automóveis",
    "automóvel": "Automóveis",
    "carros": "Automóveis",
    "carro": "Automóveis",
    "auto": "Automóveis",
    
    # Animais / Pet
    "animais": "Animais",
    "animal": "Animais",
    "pet": "Animais",
    
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
    
    # Outros
    "sem categoria": "Outros",
    "outros": "Outros",
    "other": "Outros",
    "undefined": "Outros",
    "brazil": "TVs Abertas",
    "brasil": "TVs Abertas",

    "alta definição ( hd,fhd )": "TVs Abertas",
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

# Keywords that if present in the raw name (after lower) map to category
CONTAINS_MAP = [
    ("notícia", "Notícias"),
    ("noticia", "Notícias"),
    ("news", "Notícias"),
    ("jornal", "Notícias"),
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
    ("evangélic", "Religiosos"),
    ("evangelic", "Religiosos"),
    ("gospel", "Religiosos"),
    ("católic", "Religiosos"),
    ("catolic", "Religiosos"),
    ("religio", "Religiosos"),
    ("culinár", "Culinária"),
    ("culinari", "Culinária"),
    ("cooking", "Culinária"),
    ("educativ", "Educativos"),
    ("educaç", "Educativos"),
    ("education", "Educativos"),
    ("cultur", "Cultura"),
    ("automó", "Automóveis"),
    ("automov", "Automóveis"),
    ("carro", "Automóveis"),
    ("animal", "Animais"),
    ("pet", "Animais"),
    ("televenda", "Televendas"),
    ("agro", "Agronegócio"),
    ("rural", "Agronegócio"),
    ("abert", "TVs Abertas"),
    ("regional", "TVs Abertas"),
    ("webtv", "TVs Abertas"),
    ("internacional", "Internacional"),

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
    ("hallo", "Hallo"),
    ("pluto", "Pluto TV"),
    ("Urban", "Urban TV"),
    ("Runtime", "Runtime TV")
]


def normalize_category(raw: str) -> str:
    if not raw:
        return "Outros"
    original = raw.strip()
    key = original.lower()
    
    # Exact match first
    if key in CATEGORY_SYNONYMS:
        return CATEGORY_SYNONYMS[key]
    
    # Contains / partial
    for fragment, cat in CONTAINS_MAP:
        if fragment in key:
            return cat
    
    # Title-case the original if nothing matches (but clean a bit)
    # Avoid very long or weird names becoming categories
    if len(original) > 40 or ";" in original or "/" in original:
        return "Outros"
    
    return original.title() if original else "Outros"
