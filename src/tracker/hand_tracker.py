from typing import List, NamedTuple

from mediapipe.python.solutions.drawing_utils import draw_landmarks, DrawingSpec
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS
from numpy import ndarray

from src.model.color import Color
from src.tracker.tracker import Tracker


class HandTracker(Tracker):
    _results: NamedTuple

    def __init__(self):
        self._solution = Hands(max_num_hands=1, model_complexity=0, min_detection_confidence=0.8,
                               min_tracking_confidence=0.6)

    def track(self, image: ndarray, draw: bool = True) -> ndarray:
        self._results = self._solution.process(image)

        # Draw marks on the hand image
        if self._results.multi_hand_landmarks:
            for hand_landmarks in self._results.multi_hand_landmarks:
                if draw:
                    draw_landmarks(
                        image,
                        hand_landmarks,
                        HAND_CONNECTIONS,
                        landmark_drawing_spec=DrawingSpec(color=Color.RED.color)
                    )
        return image

    def get_landmarks(self, image: ndarray) -> list:
        landmarks: List[List[int, int, int]] = []
        if self._results.multi_hand_landmarks:
            for hand_landmarks in self._results.multi_hand_landmarks:
                for (i, landmark) in enumerate(hand_landmarks.landmark):
                    height, width, _ = image.shape
                    x = int(landmark.x * width)
                    y = int(landmark.y * height)
                    landmarks.append([i, x, y])
        return landmarks
