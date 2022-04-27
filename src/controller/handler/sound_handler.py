from src.controller.handler.base_handler import BaseHandler
from src.manager.manager import Manager
from src.manager.sound.sound_manager import SoundManager


class SoundHandler(BaseHandler):

    def run(self):
        sound_manager: Manager = SoundManager()
        if not sound_manager.has_camera():
            print("No camera device was found. Turning off the sound manager..")
            sound_manager.stop()
        else:
            sound_manager.start()
