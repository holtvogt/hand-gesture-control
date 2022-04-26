from enum import Enum


class GestureMode(Enum):
    SOUND = ("Sound Control", 0)

    def __init__(self, mode_name: str, mode_number: int):
        self.mode_name = mode_name
        self.mode_number = mode_number
