from math import hypot

from cv2 import VideoCapture, circle, line, imshow, flip, FILLED, resize, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH, \
    rectangle
from mediapipe.python.solutions.hands import HandLandmark
from numpy import interp

from src.manager.manager import Manager
from src.model.color import Color
from src.model.gesture_mode import GestureMode
from src.tracker.hand_tracker import HandTracker


class SoundManager(Manager):
    """The sound manager class used to control the sound of a device using a tracker as motion control."""

    _CIRCLE_RADIUS: int = 10
    _LINE_THICKNESS: int = 3
    _MIN_DISTANCE: int = 30
    _MAX_DISTANCE: int = 300

    def __init__(self):
        """Initializes the sound manager."""

        self._tracker = HandTracker()
        self._capture = VideoCapture(self._DEFAULT_CAMERA)

    def start(self):
        while self._capture.isOpened():
            success, frame = self._capture.read()
            if not success:
                continue

            width = int(self._capture.get(CAP_PROP_FRAME_WIDTH) * 1.5)
            height = int(self._capture.get(CAP_PROP_FRAME_HEIGHT) * 1.5)
            frame = resize(frame, (width, height))

            image = self._tracker.track(frame)
            landmarks = self._tracker.get_landmarks(image)

            # Draw volume bar
            bar_width: int = int(width * 0.1)
            bar_height: int = int(height * 0.7)
            # Start 5% from the right (actually left, but mirror the frame later)
            bar_x_start: int = int(width * 0.05)
            bar_y_start: int = (height - bar_height) // 2
            bar_x_end: int = bar_x_start + bar_width
            bar_y_end: int = bar_y_start + bar_height
            rectangle(image, (bar_x_start, bar_y_start), (bar_x_end, bar_y_end), Color.BLACK.color, FILLED)

            if len(landmarks) != 0:
                # Get thumb position
                x1 = landmarks[HandLandmark.THUMB_TIP][1]
                y1 = landmarks[HandLandmark.THUMB_TIP][2]
                thumb_position = (x1, y1)
                # Get index finger position
                x2 = landmarks[HandLandmark.INDEX_FINGER_TIP][1]
                y2 = landmarks[HandLandmark.INDEX_FINGER_TIP][2]
                index_finger_position = (x2, y2)
                # Center between thumb and index finger
                x3 = (x1 + x2) // 2
                y3 = (y1 + y2) // 2
                center_position = (x3, y3)
                # Mark line between thumb and index finger
                circle(image, thumb_position, self._CIRCLE_RADIUS, Color.RED.color, FILLED)
                circle(image, index_finger_position, self._CIRCLE_RADIUS, Color.RED.color, FILLED)
                circle(image, center_position, self._CIRCLE_RADIUS, Color.RED.color, FILLED)
                line(image, thumb_position, index_finger_position, Color.RED.color, self._LINE_THICKNESS)

                # Finger distance represents volume
                finger_distance: int = int(hypot(abs(x1 - x2), abs(y1 - y2)))
                # We interpolate the finger distance on to the volume range
                volume_bar: int = int(
                    interp(finger_distance, [self._MIN_DISTANCE, self._MAX_DISTANCE], [bar_y_end, bar_y_start])
                )
                # Keep in mind that the coordinate system begins on the top left of the image
                rectangle(image, (bar_x_start, volume_bar), (bar_x_end, bar_y_end), Color.WHITE.color, FILLED)

            # Mirror selfie video
            imshow(GestureMode.SOUND.mode_name, flip(image, 1))

            if self._exit_was_pressed():
                break

        self.stop()
