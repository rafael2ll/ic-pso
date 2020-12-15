from abc import ABC, abstractmethod
from typing import Any

import tsplib95


class ParentExtractor(ABC):
    @abstractmethod
    def extract_parent(self, data: tsplib95, population: Any) -> Any:
        pass
