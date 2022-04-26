from controller.handler.sound_handler import SoundHandler


class Controller:
    _handlers: dict

    def __init__(self):
        self._init_handlers()

    def _init_handlers(self):
        self._handlers = {0: SoundHandler()}

    def get_handlers(self) -> dict:
        return self._handlers
