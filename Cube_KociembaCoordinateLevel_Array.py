from Cube import *

# http://kociemba.org/cube.htm
# Implemented with four arrays instead of four ints
class Cube_KociembaCoordinateLevel_Array(Cube):
    def __init__(self, magnitude=3):
        assert(magnitude == 3)
        super().__init__(magnitude)

    def reset():
        self.edges_permutation = range(12)
        self.edges_orientation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.corners_permutation = range(8)
        self.corners_orientation = [0, 0, 0, 0, 0, 0, 0, 0]

    def apply_move(self, move, modifer):
        assert(move in Move)
        assert(modifer in Modifer)
        if(move == Move.U and modifer == Modifer.Normal):
#            edge_permutation = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11]
#            self.edges_permutation = map(self.edges_permutation.__getitem__, 
#                                         edge_permutation)
            temp_edge = self.edges_permutation[0]
            self.edges_permutation[0] = self.edges_permutation[1]
            self.edges_permutation[1] = self.edges_permutation[2]
            self.edges_permutation[2] = self.edges_permutation[3]
            self.edges_permutation[3] = temp
            corner_permutation = [1, 2, 3, 0, 4, 5, 6, 7]
            self.corners_permutation = map(self.corners_permutation.__getitem__, 
                                         corner_permutation)

    def apply_alg(self, alg):
        moves = alg.split(" ")
        for move in moves:
            self.apply_move_string(move)

    def apply_move_string():
        move = Move.U
        modifier = Modifier.Normal
        if("'" in moveString):
            modifier = Modifier.Prime
        elif("2" in moveString):
            modifier = Modifier.Twice
        if("U" in moveString):
            move = Move.U
        elif("D" in moveString):
            move = Move.D
        elif("L" in moveString):
            move = Move.L
        elif("R" in moveString):
            move = Move.R
        elif("F" in moveString):
            move = Move.F
        elif("B" in moveString):
            move = Move.B
        self.apply_move(move, modifier)