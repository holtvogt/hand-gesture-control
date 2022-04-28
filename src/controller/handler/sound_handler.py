from src.controller.handler.base_handler import BaseHandler
from src.manager.manager import Manager
from src.manager.sound.sound_manager import SoundManager


class SoundHandler(BaseHandler):

    def run(self):
        sound_manager: Manager = SoundManager()
        if not sound_manager.video_capturing_enabled():
            print("Video capturing not enabled. Turning off the sound manager..")
            sound_manager.stop()
        else:
            sound_manager.start()
