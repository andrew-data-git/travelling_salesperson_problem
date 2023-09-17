import tsp
import utils

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    points = utils.points_generator(20,5,200)
    travel = tsp.TravellingSalesperson(points, verbose = False)
    travel.run_tsp("greedy")