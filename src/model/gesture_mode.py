from enum import Enum


class GestureMode(Enum):
    """Representing the available gesture modes."""

    SOUND = ("Sound Control", 0)

    def __init__(self, mode_name: str, mode_number: int):
        """Initializes a gesture mode.

        :param mode_name: The mode name
        :param mode_number: The corresponding mode number
        """

        self.mode_name = mode_name
        self.mode_number = mode_number
