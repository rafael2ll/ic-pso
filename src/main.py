# %%

import logging

import tsplib95

from pso import Swarm

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)
    problem = tsplib95.load('../data/gr24.tsp')
    print(problem.get_edges())
    swarm = Swarm(problem)
    swarm.submit(100)
