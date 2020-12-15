from abc import ABC, abstractmethod
from typing import Any


class Fitness(ABC):
    @abstractmethod
    def calc(self, chromosome: Any) -> float:
        pass
