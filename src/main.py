# %%

import logging

import numpy as np
import tqdm as tqdm
import tsplib95
from joblib import Parallel, delayed

from pso import CPSO
from pso.base.discrete_pso import DPSO


def run_discrete_bench(i, problem):
    dpso = DPSO(problem)
    return (i, dpso.submit(100))


def run_continue_bench(i, problem):
    cpso = CPSO(problem)
    return (i, cpso.submit(100))


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)
    problem = tsplib95.load('../data/gr48.tsp')
    CPSO(problem).submit(10)
    discrete = Parallel(n_jobs=10)(delayed(run_discrete_bench)(i, problem) for i in tqdm.tqdm(range(10)))
    continue_ = Parallel(n_jobs=10)(delayed(run_continue_bench)(i, problem) for i in tqdm.tqdm(range(10)))

    discrete = [a[1][0] for a in discrete]
    continue_ = [a[1][0] for a in continue_]
    print(f"Media CPSO:{np.mean(continue_)} \t Minima CPSO: {np.min(continue_)}")
    print(f"Media DPSO:{np.mean(discrete)} \t Minima DPSO: {np.min(discrete)}")
