from abc import abstractmethod, ABC


class BaseHandler(ABC):
    """A base handler class providing methods for a handler."""

    @abstractmethod
    def run(self):
        """Runs the handler."""
