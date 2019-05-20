from search import FifteenPuzzle
from math import *

class FifteenPuzzleMissManh(FifteenPuzzle):
    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles + Manhattan distance """
        mMissManh = sum( (s != g) + (abs(s%4 - g%4) + abs(s/4 - g/4)) for (s, g) in  zip(node.state, self.goal))
        return mMissManh

class FifteenPuzzleEuclidian(FifteenPuzzle):
    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = Euclidian distance """
        mEucl = sum(sqrt((s%4 - g%4)**2 + (s/4 - g/4)**2) for (s, g) in zip(node.state, self.goal))
        return mEucl