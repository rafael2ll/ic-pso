import random

import numpy as np
import tsplib95

from pso.base.particle import DParticle
from utils.logger import get_logger

logger = get_logger(__name__)


def fit(path, problem):
    cyclic_path = np.hstack((path, np.array([path[0]])))
    return sum(problem.get_weight(a, b) for a, b in zip(cyclic_path[0:], cyclic_path[1:]))


def discrete_velocity(particle: DParticle):
    return random.choices(particle.velocity, k=np.random.randint(len(particle.position)))


def velocity_idx(problem: tsplib95, vi: np.array, yi: np.array, xi: np.array, y_best: np.array, c1: float, c2: float):
    r1 = np.random.uniform(-1, 1, xi.shape)
    r2 = np.random.uniform(-1, 1, xi.shape)
    logger.debug(f"Original F: {vi} + {c1} * {r1} * ({yi} - {xi}) + {c2} * {r2} * ({y_best} - {xi})")
    v = np.abs(np.array(vi + c1 * r1 * (yi - xi) + c2 * r2 * (y_best - xi), dtype=np.int64))
    logger.debug(f"Velocity: {v}")
    return v


def adjust_discrete_position(particle: DParticle, velocity: np.array):
    for exchange in velocity:
        tmp = np.copy(particle.position[exchange[0]])
        particle.position[exchange[0]] = particle.position[exchange[1]]
        particle.position[exchange[1]] = tmp


def correct_path(position: np.array, problem_size):
    corr = []
    for a in position:
        if a not in corr:
            corr.append(a)
        else:
            corr.append(-1)

    for i in range(problem_size):
        if corr[i] == -1:
            corr[i] = random.choice([b for b in range(problem_size) if b not in corr])
    return np.array(corr)


if __name__ == '__main__':
    vi = np.array([1, 2, 3, 4, 5])
    yi = np.array([6, 7, 8, 9, 10])
    xi = np.array([15, 16, 17, 18, 19])
    y_best = np.array([25, 26, 28, 30, 35])
    C1 = np.random.random()
    C2 = np.random.random()
    print(velocity_idx(vi, yi, xi, y_best, C1, C2))
