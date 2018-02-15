import youtube_dl


def get_best_audio_link(url):
    with youtube_dl.YoutubeDL(dict(quiet=True)) as ytdl:
        result = ytdl.extract_info(url, download=False)

    best_url = ''
    best_id = 0
    if not result.get('formats'):
        return best_url
    for fmt in result['formats']:

        if fmt.get('format_note', '') != 'DASH audio': continue
        try:
            id_num = int(fmt['format_id'])
        except ValueError:
            continue
        if id_num > best_id:
            best_id = int(fmt['format_id'])
            best_url = fmt['url']

    return best_url
