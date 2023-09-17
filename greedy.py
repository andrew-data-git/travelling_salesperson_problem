"""
Conducts a greedy method to solve the TSP.

        Parameters
        ----------
            points : list of tuples
                 Collection of x,y pairs for algorithm to be run on.
"""
import random
import sys
import utils

def greedy(points):
    """
    A simple greedy algorithm that visits all points without repeating.

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
    visited = [False]*num_points # to store which cities covered
    tour = []
    cost = 0
    start = random.randint(0, num_points) # randomly select a starting number
    visited[start] = True # visit the start
    tour = [start] # append to this list

    # calculate euclidean distances between all points and save as a matrix called graph
    graph = utils.graph_generator(points)

    # apply the greedy algorithm - take the closest unvisited point to the current one
    for _ in range(num_points - 1):
        min_cost = sys.maxsize # create holding variables for cost and next point
        next_point = None

        for point in range(num_points):
            if not visited[point] and graph[tour[-1]][point] < min_cost:
                next_point = point
                min_cost = graph[tour[-1]][point]

        tour.append(next_point)
        visited[next_point] = True
        cost += min_cost

    cost += graph[tour[-1]][0]  # Return to the start
    tour.append(0)

    # finally return the points ordered by tour
    tour_points = sorted(zip(tour, points), key=lambda pair: pair[0])
    return tour_points
