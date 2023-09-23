import tsp
import utils

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    points = utils.points_generator(200, 0, 5000) # defaults are num_points = 10, min = 0, max = 100
    travel = tsp.TravellingSalesperson(points, verbose=False)
    travel.run_tsp("greedy")