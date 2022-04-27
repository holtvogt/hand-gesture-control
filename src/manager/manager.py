from abc import abstractmethod

from cv2 import VideoCapture, destroyAllWindows

from src.tracker.tracker import Tracker


class Manager:
    _DEFAULT_CAMERA: int = 0

    _tracker: Tracker
    _capture: VideoCapture

    @abstractmethod
    def start(self):
        """Starts the controller."""

    def stop(self):
        self._capture.release()
        destroyAllWindows()
