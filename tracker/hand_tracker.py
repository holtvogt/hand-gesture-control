from typing import NamedTuple

from mediapipe.python.solutions.drawing_styles import get_default_hand_landmarks_style, \
    get_default_hand_connections_style
from mediapipe.python.solutions.drawing_utils import draw_landmarks
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS
from numpy import ndarray

from tracker.tracker import Tracker


class HandTracker(Tracker):
    _results: NamedTuple

    def __init__(self):
        self._solution = Hands(max_num_hands=1, model_complexity=0, min_detection_confidence=0.7)

    def track(self, image, draw: bool = True) -> ndarray:
        self._results = self._solution.process(image)

        # Draw marks on the hand image
        if self._results.multi_hand_landmarks:
            for hand_landmarks in self._results.multi_hand_landmarks:
                if draw:
                    draw_landmarks(
                        image,
                        hand_landmarks,
                        HAND_CONNECTIONS,
                        get_default_hand_landmarks_style(),
                        get_default_hand_connections_style()
                    )
        return image

    def get_landmarks(self, image) -> list:
        landmarks = []
        if self._results.multi_hand_landmarks:
            for hand_landmarks in self._results.multi_hand_landmarks:
                for (i, landmark) in enumerate(hand_landmarks.landmark):
                    height, width, _ = image.shape
                    x = int(landmark.x * width)
                    y = int(landmark.y * height)
                    landmarks.append([i, x, y])
        return landmarks
