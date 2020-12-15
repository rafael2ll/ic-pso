from abc import ABC, abstractmethod


class Representation(ABC):
    @abstractmethod
    def get(self):
        pass
