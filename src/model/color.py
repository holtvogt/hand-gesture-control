from enum import Enum


class Color(Enum):
    """Represents a color in BGR format."""

    WHITE = (224, 224, 224)
    BLACK = (0, 0, 0)
    RED = (0, 0, 255)
    GREEN = (0, 128, 0)
    BLUE = (255, 0, 0)

    def __init__(self, blue_value: int, green_value: int, red_value: int):
        self.color: tuple = (blue_value, green_value, red_value)
