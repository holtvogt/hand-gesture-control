from abc import abstractmethod

from cv2 import VideoCapture, destroyAllWindows, waitKey

from src.model.button import Button
from src.tracker.tracker import Tracker


class Manager:
    """A base manager class providing methods to use a tracker within a video capturing output."""

    _DEFAULT_CAMERA: int = 0
    _EXIT_BUTTON: int = Button.ESCAPE.value
    _MINIMUM_WAIT: int = 10

    _tracker: Tracker
    _capture: VideoCapture

    @abstractmethod
    def start(self):
        """Starts the manager."""

    def stop(self):
        """Stops the manager."""

        self._capture.release()
        destroyAllWindows()

    def video_capturing_enabled(self):
        """Checks whether video capturing via camera enabled.

        :return: True, if video capturing is successfully initialized, false otherwise
        """

        return self._capture.isOpened()

    def _exit_was_pressed(self) -> bool:
        """Checks if the corresponding exit button was pressed to close video capturing.

        :return: True, if the button was pressed, false otherwise
        """

        return (waitKey(self._MINIMUM_WAIT) & 0xFF) == self._EXIT_BUTTON
