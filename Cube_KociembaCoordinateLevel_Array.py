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
            # Cycles edges in U layer clockwise
            # The U layer edges, listed clockwise, are 3, 2, 1, 0
            temp_edge = self.edges_permutation[0]
            self.edges_permutation[0] = self.edges_permutation[1]
            self.edges_permutation[1] = self.edges_permutation[2]
            self.edges_permutation[2] = self.edges_permutation[3]
            self.edges_permutation[3] = temp_edge
            # Cycles corners in U layer clockwise
            # The U layer corners, listed clockwise, are 3, 2, 1, 0
            temp_corner = self.corners_permutation[0]
            self.corners_permutation[0] = self.corners_permutation[1]
            self.corners_permutation[1] = self.corners_permutation[2]
            self.corners_permutation[2] = self.corners_permutation[3]
            self.corneres_permutation[3] = temp_corner
        if(move == Move.U and modifer == Modifer.Twice)
            pass

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