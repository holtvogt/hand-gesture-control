from src.controller.handler.sound_handler import SoundHandler


class Controller:
    """A controller class used for controlling handlers."""

    _handlers: dict

    def __init__(self):
        """Initializes the controller."""

        self._init_handlers()

    def _init_handlers(self):
        """Initializes the available handlers."""

        self._handlers = {0: SoundHandler()}

    def get_handlers(self) -> dict:
        """Gets the handlers.

        :return: The available handlers
        """

        return self._handlers
