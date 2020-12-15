from abc import ABC, abstractmethod
from typing import Any


class Mutation(ABC):
    @abstractmethod
    def apply(self, offspring: Any, rate: float = 0.01) -> Any:
        pass
