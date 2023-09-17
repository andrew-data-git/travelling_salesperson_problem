"""
Conducts the branch-and-bound method to solve the TSP.
Adapted from ChatGPT code.

        Parameters
        ----------

"""

import random
import sys
import utils
from utils import default_points
import numpy as np

points = default_points

def random_path(points):
    """
    Solving the TSP in probably the least efficient manner.

    Parameters
    ----------
        points : list of tuples
             Collection of x,y pairs for algorithm to be run on.

    Outputs
    -------
        tour_points : tuple of tuples
            Of the form (k,(x,y)), where k is the position in the generated tour that (x,y) is visited.
    """
    # variables
    num_points = len(points)
    cost = 0
    tour = [0]  # append to this list

    # shuffle the points
    random.shuffle(points)

    # calculate euclidean distances between all points and save as a matrix called graph
    graph = utils.graph_generator(points)

    # apply the random algorithm - take any unvisited point and move there
    for _ in range(num_points - 1):
        for point in range(num_points):
            path_cost = graph[tour[-1]][point]
        tour.append(point)
        cost += path_cost

    cost += graph[tour[-1]][0]  # Return to the start
    tour.append(0)

    # finally return the points ordered by tour
    tour_points = sorted(zip(tour, points), key=lambda pair: pair[0])
    return tour_points