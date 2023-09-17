"""
Conducts the branch-and-bound method to solve the TSP.

        Parameters
        ----------

"""

import random
import sys

import numpy as np

import utils
from utils import default_points

points = default_points[0:4]


def branchbound(points):
    """
    Solving the TSP by the branch and bound algorithm.

    Parameters
    ----------
        points : list of tuples
             Collection of x,y pairs for algorithm to be run on.

    Outputs
    -------
        tour_points : tuple of tuples
            Of the form (k,(x,y)), where k is the position in the generated tour that (x,y) is visited.
    """

    # calculate euclidean distances between all points and save as a matrix called graph
    graph = utils.graph_generator(points)
    #utils.graph_plotter(points)
    print(np.array(graph))

branchbound(points)
