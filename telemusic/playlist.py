import vlc
from youtube_dl.utils import DownloadError

from .audio_link_getter import get_best_audio_link
from .helpers import get_channel


class Playlist:
    def __init__(self, bot, queue=None):
        self._bot = bot
        self._queue = []
        if queue:
            for item in queue:
                if item:
                    self.add(item)
        self._vlc_instance = vlc.Instance()
        self._player = self._vlc_instance.media_player_new()
        self._playing = ''
        self._paused = True

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._queue) == 0:
            raise StopIteration
        url = self._queue.pop(0)
        return url

    @property
    def queue(self):
        return self._queue.copy()

    @property
    def playing(self):
        return self._playing

    def add(self, url, duplicate=True):

        if not duplicate and url in self._queue:
            # already in queue, so don't add again
            return

        self._queue.append(url)

    def update(self, skip=False):

        if self._paused:
            return True  # there is a file to play but it isn't playing

        while True:
            if skip or not (self._player.is_playing() or self._player.will_play()):
                try:
                    next_url = next(self)
                except StopIteration:
                    self._paused = True  # require hitting play again.
                    self._playing = ''
                    return False  # there's no more files to play
                self._playing = next_url
                try:
                    best_link = get_best_audio_link(next_url)
                    if not best_link:
                        continue
                    if not best_link.startswith('http'):
                        continue  # naive protection against accessing local files
                    media = self._vlc_instance.media_new(best_link)
                    media.get_mrl()
                except DownloadError:
                    continue
                self._player.set_media(media)
                self.message_channel()
                self._player.play()

            return True  # there is a file playing

    def play(self):
        if self._paused:
            self._player.play()
            self._paused = False
        self.update()

    def pause(self):
        self._player.pause()
        self._paused = True

    def skip(self):
        self._player.stop()
        self._playing = ''
        self.update(skip=True)

    def message_channel(self):
        channel = get_channel()
        if channel:
            chat = self._bot.tg.chat(chat_id=channel)
            self._bot.nowplaying_helper(chat)
