"""Generic supporting functions."""
import numpy as np
import random
import matplotlib.pyplot as plt
import itertools
from matplotlib import collections as mc

def euclid(point1, point2):
    """Calculates hypotenuse length.

    Parameters
    ----------
        point1 : int
             Rise.
        point2 : int
             Run.
    """
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def points_generator(num_points = 10, min = 0, max = 100):
    """
    A function to create a quantity of (x,y) points given a certain min and max.

    Parameters
    ----------
        num_points : int
             How many points require generation.
        min, max : int, int
             Min and max for random ints.
    """
    points = []
    for i in range(num_points):
        points.append((random.randint(min, max),random.randint(min, max)))
    return points

def graph_generator(points):
    """
    Creates a symetrical matrix of distances between points.

    Parameters
    ----------
        points : list
            A list (x,y) points to be evauluated.
    """
    num_points = len(points)
    # calculate euclidean distances between all points and save as a matrix called graph
    graph = [[0 for _ in range(num_points)] for _ in range(num_points)] # empty matrix of num_points x num_points
    for i in range(num_points):
        for j in range(i+1,num_points):
            dist = euclid(points[i], points[j])
            graph[i][j] = graph[j][i] = dist # a symetrical matrix
    return graph

def graph_plotter(points):
    """Draws all possible line segments."""
    lines = list(itertools.combinations(points, 2))
    line_collection = mc.LineCollection(lines, linewidths=1)
    fig, ax = plt.subplots()
    ax.add_collection(line_collection)
    ax.autoscale()
    plt.show(block=False)

# if random points not required
default_points = [(0,0),(3,4),(92,29),(18,5),(36,83),(77,100),(22,47),(7,26),(1,29),(89,58),(59,48),(7,5),(93,69)]
