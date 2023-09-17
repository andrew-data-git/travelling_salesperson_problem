"""Travelling salesperson algorithm."""
import random
import time
import matplotlib.pyplot as plt
import itertools
import numpy as np
from matplotlib import collections as mc
import greedy


class TravellingSalesperson:
    """
    A class that contains points and methods for visualising the travelling salesperson algorithm.

    ...

    Attributes
    ----------
    points : list of tuples
        Collection of x,y pairs for algorithm to be run on.

    Methods
    -------
    print_points :
        Prints the points in friendly mode.
    plot_points :
        Plots all the points and draws lines between them.
    """

    def __init__(self, points, algorithm, verbose = False):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            points : list of tuples
                 Collection of x,y pairs for algorithm to be run on.
            algorithm : str
                 Includes "greedy", ... ; selects which TSP algorithm to run.
        """
        self.points = points
        self.algorithm = algorithm
        self.verbose = verbose
        print(f"Generating path covering all points by {self.algorithm} algorithm...")
        self.draw_lines()
        self.tour_points = self.run_tsp()
        self.plot_tsp()

    def print_points(self):
        """Prints points to console."""
        # print("Input coordinates are:")
        print(self.points)

    def draw_lines(self):
        """Draws all possible line segments."""
        lines = list(itertools.combinations(self.points, 2)) # create line segments
        if self.verbose == True: print(f"Created {len(lines)} line segments.")

        # plot in matplotlib
        line_collection = mc.LineCollection(lines, linewidths=1)
        fig, ax = plt.subplots()
        ax.add_collection(line_collection)
        ax.autoscale()
        print("3")
        plt.pause(1)
        print("2")
        plt.pause(1)
        print("1")
        plt.pause(1)
        print("Go!")
        #plt.show(block=False)

    def run_tsp(self):
        """Call an algorithm to solve the travelling salesperson problem."""
        tour_points = greedy.greedy(self.points)
        if self.verbose == True:
            print("Route is :")
            print(tour_points)
        return tour_points

    def plot_tsp(self):
        """Draws the toured points line segments and labels with number."""

        # create the list of segments
        segments = []
        for i in range(len(self.tour_points) - 1):
            segment = (self.tour_points[i][1], self.tour_points[i + 1][1])
            segments.append(segment)
        segments.append((self.tour_points[-1][1], self.tour_points[0][1]))  # return to the start again

        # plot in matplotlib with label
        line_collection = mc.LineCollection(segments, linewidths=1, colors="red")
        fig, ax = plt.subplots()
        ax.add_collection(line_collection)
        for k, point in enumerate(self.tour_points):
            x = point[1][0]
            y = point[1][1]
            ax.annotate(k, (x, y))  # ,
            # xytext=(x+random.randint(2,6), y-random.randint(4,8)), arrowprops = dict(arrowstyle="->"))
        ax.autoscale()
        print("Complete.")
        plt.show()
