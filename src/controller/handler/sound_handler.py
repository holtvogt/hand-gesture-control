from src.controller.handler.base_handler import BaseHandler
from src.manager.manager import Manager
from src.manager.sound.sound_manager import SoundManager


class SoundHandler(BaseHandler):

    def run(self):
        sound_manager: Manager = SoundManager()
        sound_manager.start()
