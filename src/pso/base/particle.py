import numpy as np


class CParticle:
    def __init__(self, path: np.array):
        self.position = path
        self.velocity = np.random.uniform(1, 5, size=(len(path)))
        self.best_position = np.copy(self.position)
        self.best_path_len = np.inf

    def __str__(self):
        return f"{{BL: {self.best_path_len}, BP: {self.best_position}, CP: {self.position}, V: {self.velocity}}}\n"

    def __repr__(self):
        return self.__str__()


class DParticle:
    def __init__(self, path: np.array):
        self.position = path
        self.combination_count = np.random.randint(len(path) * (len(path) - 1)) + 1
        self.velocity = np.random.randint(len(path), size=(self.combination_count, 2))
        self.best_position = np.copy(self.position)
        self.best_path_len = np.inf

    def __str__(self):
        return f"{{BL: {self.best_path_len}, BP: {self.best_position}, CP: {self.position}, V: {self.velocity}}}\n"

    def __repr__(self):
        return self.__str__()
