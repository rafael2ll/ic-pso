import math
from typing import List

import numpy as np

from pso.base.adjuster import fit, correct_path, velocity_idx
from pso.base.particle import Particle
from utils.logger import get_logger

logger = get_logger(__name__)


class Swarm:
    def __init__(self, problem, size=100):
        self.problem = problem
        self.length = len(list(problem.get_nodes()))

        self.C1 = np.random.random()
        self.C2 = np.random.random()

        self.best_path = math.inf
        self.best_path_pos = np.random.permutation(range(len(list(self.problem.get_nodes()))))

        permutations = np.array([
            np.random.permutation(range(len(list(self.problem.get_nodes())))) for _ in list(range(size))])
        self.particles: List[Particle] = [Particle(perm) for perm in permutations]
        logger.debug(f"Initial swarm[{self.length}]:\n{self.particles}")

    def submit(self, iterations=1000):
        for i in range(iterations):
            for particle in self.particles:
                particle.velocity = velocity_idx(self.problem,
                                                 particle.velocity,
                                                 particle.best_position,
                                                 particle.position,
                                                 self.best_path_pos,
                                                 self.C1, self.C2)

                particle.position += particle.velocity
                logger.debug(f'No change: {particle.position}')

                particle.position[particle.position >= self.length] = self.length - 1
                logger.debug(f'Adjusted outliers: {particle.position}')

                particle.position = correct_path(particle.position, self.length)
                logger.debug(f'Corrected Path: {particle.position}')

                distance = fit(particle.position, self.problem)
                logger.debug(f"Distance: {distance}\t Path:{particle.position}")

                # Is it the best particle distance so far?
                if distance < particle.best_path_len:
                    particle.best_position = np.copy(particle.position)
                    particle.best_path_len = distance
                    # May be the best global distance as well?
                    if distance < self.best_path:
                        self.best_path = distance
                        self.best_path_pos = np.copy(particle.position)
                        logger.info(f"Best distance: {self.best_path}\tBest Path:{self.best_path_pos}")

        logger.info(f"{':' * 5} Best distance: {self.best_path}\tBest Path:{self.best_path_pos} {':' * 5}")
