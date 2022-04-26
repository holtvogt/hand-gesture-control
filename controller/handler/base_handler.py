from abc import abstractmethod, ABC


class BaseHandler(ABC):

    @abstractmethod
    def run(self):
        """Runs the handler."""
