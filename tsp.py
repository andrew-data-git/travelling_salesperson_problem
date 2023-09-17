"""Travelling salesperson algorithm."""
import random
import time
import matplotlib.pyplot as plt
import itertools
import numpy as np
from matplotlib import collections as mc
import greedy
import random_path


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

    def __init__(self, points, verbose = False):
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
        self.verbose = verbose

    def print_points(self):
        """Prints points to console."""
        # print("Input coordinates are:")
        print(self.points)

    def make_graph(self):
        """Draws all possible line segments."""
        lines = list(itertools.combinations(self.points, 2)) # create line segments
        if self.verbose == True: print(f"Created {len(lines)} line segments.")

        # plot in matplotlib
        graph_lines = mc.LineCollection(lines, linewidths=1)
        return graph_lines

    def pick_tsp(self, algorithm):
        """Call an algorithm to solve the travelling salesperson problem."""
        tour_points = None
        if algorithm == "greedy":
            tour_points = greedy.greedy(self.points)
        elif algorithm == "random_path":
            tour_points = random_path.random_path(self.points)
        else:
            print("ERROR")
        if self.verbose == True:
            print("Route is :")
            print(tour_points)
        return tour_points

    def run_tsp(self, algorithm = "greedy"):
        """Docstring"""
        if algorithm in ["greedy","random_path"]:
            print(f"Generating path covering all points by {algorithm} algorithm...")
            self.tour_points = self.pick_tsp(algorithm)
            self.plot_tsp()
        else:
            print("Algorithm not in list!")

    def make_solution(self):
        # create the list of segments
        segments = []
        for i in range(len(self.tour_points) - 1):
            segment = (self.tour_points[i][1], self.tour_points[i + 1][1])
            segments.append(segment)
        segments.append((self.tour_points[-1][1], self.tour_points[0][1]))  # return to the start again
        solution_lines = mc.LineCollection(segments, linewidths=1, colors="red")
        return solution_lines

    def plot_tsp(self):
        """Draws the toured points line segments and labels with number."""
        # plot in matplotlib with label
        graph_lines = self.make_graph()
        solution_lines = self.make_solution()
        fig, ax = plt.subplots()
        ax.add_collection(graph_lines)
        ax.autoscale()
        print("3")
        plt.pause(1)
        print("2")
        plt.pause(1)
        print("1")
        plt.pause(1)
        print("Go!")
        ax.add_collection(solution_lines)
        for k, point in enumerate(self.tour_points):
            x = point[1][0]
            y = point[1][1]
            ax.annotate(k, (x, y), xytext=(x+10, y+15), arrowprops = dict(arrowstyle="->"))
        ax.autoscale()
        print("Complete.")
        plt.show()



