from pawt.bots import MappedCommandBot

from .helpers import get_queue, get_listener_name, set_queue, get_listener_id, get_key
from .playlist import Playlist


class MusicBot(MappedCommandBot):
    def __init__(self, token, *, url=None, session=None):
        text_command_map = {}
        text_command_map['/start'] = self.start
        text_command_map['/help'] = self.help
        text_command_map['/add'] = self.add
        text_command_map['/play'] = self.play
        text_command_map['/pause'] = self.pause
        text_command_map['/skip'] = self.skip
        text_command_map['/id'] = self.id
        super().__init__(token, text_command_map, caption_command_map=None, url=url, session=session)

        self._playlist = Playlist(get_queue())
        self._LISTENER_NAME = get_listener_name()
        self._LISTENER_ID = get_listener_id()

    def perform_extra_task(self):
        self._playlist.update()

    def before_exit(self):
        set_queue([self._playlist.playing] + self._playlist.queue)

    @staticmethod
    def id(message, unused):
        message.chat.send_message('Your ID is {}.'.format(message.user.id))

    def start(self, message, unused):
        message.chat.send_message("Hi, I'm a music queue bot for {}.".format(self._LISTENER_NAME))
        self.help(message, unused)

    @staticmethod
    def help(message, unused):
        message.chat.send_message('My commands:\n/help: View this help message\n/add [URL]: Add this youtube URL to '
                                  "the listener's queue\n\nCommands only the listener can use:\n/play: Play the "
                                  "music\n/pause: Pause the music\n/skip: Skip to the next track")

    def add(self, message, opts):
        opts = opts.partition(' ')[2]
        url = opts.split()[0] if opts else None
        if not url:
            message.reply.send_message('Please provide a URL.')
        else:
            self._playlist.add(url)
            message.reply.send_message('This video has been added to the queue.')

    def is_listener(self, message):
        return message.user == self._LISTENER_ID

    def play(self, message, unused):
        if self.is_listener(message):
            self._playlist.play()

    def pause(self, message, unused):
        if self.is_listener(message):
            self._playlist.pause()

    def skip(self, message, unused):
        if self.is_listener(message):
            self._playlist.skip()


def run():
    bot = MusicBot(get_key())
    bot.run(timeout=5)
