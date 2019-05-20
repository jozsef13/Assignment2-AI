import time
from search import *
from P1 import *
from P2 import *

def main():
    print("Problem 1 - The Water Jug Problem - \n")
    problem_waterJug = WaterJugProblem((0, 4, 0, 3), (2, 4, 0, 3))
    path = breadth_first_tree_search(problem_waterJug).solution()
    print('Solution Path: ',path, '\n')

    print("Problem 2 - 15-puzzle Problem - \n")
    problem_missManh = FifteenPuzzleMissManh((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 0, 13, 14, 12, 11), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    problem_eucl = FifteenPuzzleEuclidian((1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 15, 13, 14, 12, 11), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
    t1 = time.time()
    missManhPath = astar_search(problem_missManh).solution()
    t2 = time.time()
    t3 = time.time()
    euclidianPath = astar_search(problem_eucl).solution()
    t4 = time.time()

    print('Solution Path 1 (Missplaced and Manhattan) : ',missManhPath, '\n Time: ', t2 - t1, '\n')
    print('Solution Path 2 (Euclidian) : ', euclidianPath, '\n Time: ', t4 - t3, '\n')

if __name__ == "__main__":
    main()
