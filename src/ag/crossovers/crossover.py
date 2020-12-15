from abc import ABC, abstractmethod
from typing import Any


class CrossOver(ABC):
    @abstractmethod
    def cross(self, parents: Any, offspring_count: int = 1, more=None) -> Any:
        pass
