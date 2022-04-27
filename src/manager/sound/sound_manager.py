from cv2 import VideoCapture, destroyAllWindows, waitKey, circle, line, imshow, flip, FILLED
from mediapipe.python.solutions.hands import HandLandmark

from src.manager.manager import Manager
from src.model.gesture_mode import GestureMode
from src.tracker.hand_tracker import HandTracker
from src.tracker.tracker import Tracker


class SoundManager(Manager):
    _DEFAULT_CAMERA: int = 0
    _CIRCLE_RADIUS: int = 15
    _BLACK: tuple = (0, 0, 0)
    _LINE_THICKNESS: int = 5

    _tracker: Tracker
    _capture: VideoCapture

    def __init__(self):
        self._tracker = HandTracker()
        self._capture = VideoCapture(self._DEFAULT_CAMERA)

    def start(self):
        while self._capture.isOpened():
            success, frame = self._capture.read()
            if not success:
                continue

            image = self._tracker.track(frame)
            landmarks = self._tracker.get_landmarks(image)

            if len(landmarks) != 0:
                # Get thumb position
                x1 = landmarks[HandLandmark.THUMB_TIP][1]
                y1 = landmarks[HandLandmark.THUMB_TIP][2]
                thumb_position = (x1, y1)
                # Get index finger position
                x2 = landmarks[HandLandmark.INDEX_FINGER_TIP][1]
                y2 = landmarks[HandLandmark.INDEX_FINGER_TIP][2]
                index_finger_position = (x2, y2)

                circle(image, thumb_position, self._CIRCLE_RADIUS, self._BLACK, FILLED)
                circle(image, index_finger_position, self._CIRCLE_RADIUS, self._BLACK, FILLED)
                line(image, thumb_position, index_finger_position, self._BLACK, self._LINE_THICKNESS)

            # Mirror selfie video
            imshow(GestureMode.SOUND.mode_name, flip(image, 1))

            if waitKey(10) & 0xFF == 27:
                break

        self.stop()

    def stop(self):
        self._capture.release()
        destroyAllWindows()
