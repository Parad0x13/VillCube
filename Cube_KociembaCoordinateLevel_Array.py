from Cube import *

# http://kociemba.org/cube.htm
# Implemented with four arrays instead of four ints
class Cube_KociembaCoordinateLevel_Array(Cube):
    def __init__(self, magnitude=3):
        assert(magnitude == 3)
        super().__init__(magnitude)
        
    def reset():
        self.edges_permutation = [Edge.UF, Edge.UR, Edge.UB, Edge.UL,
                                  Edge.FR, Edge.BR, Edge.BL, Edge.FL,
                                  Edge.DF, Edge.DR, Edge.DB, Edge.DL]
        self.edges_orientation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.corners_permutation = [Corner.UFR, Corner.UBR, Corner.UBL,
                                    Corner.UFL, Corner.DFR, Corner.DBR,
                                    Corner.DBL, Corner.DFL]
        self.corners_orientation = [0, 0, 0, 0, 0, 0, 0, 0]
        
    def apply_move(self, move, modifer):
        assert(move in Move)
        assert(modifer in Modifer)
        if(move == Move.U and modifer == Modifer.Normal):
            edge_permutation = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11]
            self.edges_permutation = map(self.edges_permutation.__getitem__, 
                                         edge_permutation)
            corner_permutation = []
        
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