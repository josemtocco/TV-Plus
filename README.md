# Lista M3U Otimizada para SS IPTV (Brasil)

Lista agregada e otimizada de canais brasileiros a partir de múltiplas fontes públicas, preparada especialmente para o aplicativo **SS IPTV**.

## Características

- **Atualização automática a cada 6 horas** via GitHub Actions
- **Persistência de canais**: canais que sumiram das fontes só são removidos após **3 atualizações consecutivas** sem aparecer (evita "piscar" de canais)
- **Deduplicação por URL**: um único canal por link de stream
- **Categorias normalizadas**:
  - Case-insensitive (Notícias = noticias = NOTÍCIAS)
  - Sinônimos unidos (Desenhos + Kids + Infantil + Criança → **Infantil**; Cinema + Filmes → **Filmes**; etc.)
- **Tiles grandes no SS IPTV**: usa `#EXTSIZE: big` para botões grandes e visualização facilitada
- Ordenação lógica das categorias e canais por nome

## Como usar no SS IPTV

1. Abra o SS IPTV na sua TV
2. Vá em **Configurações → Conteúdo → Playlists externas → Adicionar**
3. Cole a URL abaixo:

```
https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPO/main/lista_ssiptv.m3u
```

(Substitua `SEU_USUARIO/SEU_REPO` pelo caminho real do seu repositório após o fork/upload)

## Fontes utilizadas

As listas são agregadas a partir dos repositórios públicos do usuário `josemtocco` (e similares):

- olhosnatv-brasil
- ketv-m3u
- Paster
- clubecanais-m3u
- m3u-ssiptv-br
- tvgarden-br-m3u
- vidks_m3u
- batistaplay
- xttv-m3u-ssiptv
- soultv_m3u
- iptv-br-updater
- iptvcat
- IPTV-BR
- brasil-tv-m3u-scr-v3
- brasil-stream-catalog
- tv-brasil-m3u
- CanaisBR-brasil-tv-m3u-scr-v12-definitiva
- mais-sbt-m3u

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `lista_ssiptv.m3u` | Playlist final otimizada |
| `state.json` | Estado dos canais (fail_count, last_seen) para persistência |
| `update_playlist.py` | Script de agregação e normalização |
| `category_map.py` | Mapa de sinônimos de categorias |
| `.github/workflows/update.yml` | Action que roda a cada 6h |

## Rodar localmente

```bash
python3 update_playlist.py
```

## Licença

Uso livre. Os streams pertencem aos seus respectivos provedores. Esta lista apenas agrega e organiza links públicos.
