import random

import numpy as np
import tsplib95

from utils.logger import get_logger

logger = get_logger(__name__)


def fit(path, problem):
    return sum(problem.get_weight(a, b) for a, b in zip(path[0:], path[1:]))


def velocity_idx(problem: tsplib95, vi: np.array, yi: np.array, xi: np.array, y_best: np.array, c1: float, c2: float):
    r1 = np.random.uniform(-1, 1, xi.shape)
    r2 = np.random.uniform(-1, 1, xi.shape)
    logger.debug(f"Original F: {vi} + {c1} * {r1} * ({yi} - {xi}) + {c2} * {r2} * ({y_best} - {xi})")
    v = np.abs(np.array(vi + c1 * r1 * (yi - xi) + c2 * r2 * (y_best - xi), dtype=np.int64))
    logger.debug(f"Velocity: {v}")
    return v


def velocity_by_dist(problem: tsplib95, vi: np.array, yi: np.array, xi: np.array, y_best: np.array, c1: float,
                     c2: float):
    r1 = np.random.uniform(0, 1, xi.shape)
    r2 = np.random.uniform(0, 1, xi.shape)
    yi_minus_xi = np.array([problem.get_weight(y, x) for y, x in zip(yi, xi)]) * 0.01
    ybest_minus_xi = np.array([problem.get_weight(y, x) for y, x in zip(y_best, xi)]) * 0.01
    logger.debug(f"Original F: {vi} + {c1} * {r1} * ({yi} - {xi}) + {c2} * {r2} * ({y_best} - {xi})")
    logger.debug(f"Distance F: {vi} + {c1} * {r1} * ({yi_minus_xi}) + {c2} * {r2} * ({ybest_minus_xi})")
    v = np.abs(np.array(vi + c1 * r1 * yi_minus_xi + c2 * r2 * ybest_minus_xi, dtype=np.int64))
    logger.debug(f"Velocity: {v}")
    return v


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
    print(velocity(vi, yi, xi, y_best, C1, C2))
