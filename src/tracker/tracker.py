from abc import abstractmethod, ABC

from mediapipe.python.solution_base import SolutionBase
from numpy import ndarray


class Tracker(ABC):
    """Abstract tracker used to track and landmark different shapes, poses or objects in general."""

    _solution: SolutionBase

    @abstractmethod
    def track(self, image: ndarray, draw: bool = True) -> ndarray:
        """Finds certain solutions in the image.

        :return: The processed image with landmarks on
        """

    @abstractmethod
    def get_landmarks(self, image: ndarray) -> list:
        """Gets the current landmark on the image.

        :param image: The current image
        :return: The landmarks on the image
        """
