from abc import abstractmethod


class Manager:

    @abstractmethod
    def start(self):
        """Starts the controller."""

    @abstractmethod
    def stop(self):
        """Stops the controller."""
