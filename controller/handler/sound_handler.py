from controller.handler.base_handler import BaseHandler
from manager.volume.manager import Manager
from manager.volume.sound_manager import SoundManager


class SoundHandler(BaseHandler):

    def run(self):
        sound_manager: Manager = SoundManager()
        sound_manager.start()
