from abc import ABC, abstractmethod

from numpy import array


class Population(ABC):
    @abstractmethod
    def get(self, idx) -> array:
        pass

    @abstractmethod
    def get_pop(self) -> array:
        pass

    @abstractmethod
    def init(self, data, nro_chromosomes=100):
        pass

    @abstractmethod
    def add_offspring(self, offspring):
        pass

    @abstractmethod
    def natural_selection(self, beings=0):
        pass

    def set_pop(self, pop):
        pass
