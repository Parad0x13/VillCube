from utility import *
from Cube import *

# Template state system uses faces in this order 1(Up), 2(Right), 3(Front), 4(Left), 5(Back), 6(Down)
# Each face is identified by upper left to bottom right in sequence whilst viewing face from the front
# Cube_standard will be a viable cube implementation, but will not be optimized like we intend to do
#   Basically it will just be an operational state to compare optimization results against
class Cube_Standard(Cube):
    state = []      # Structure, 6 lists per face, in each face list there are magnitude amount of rows
    faces = ["U", "R", "F", "L", "B", "D"]  # Allows us to change the structure format easily

    def __init__(self, magnitude=3):
        super().__init__(magnitude)

    def reset(self):
        self.state = []
        for face in self.faces:
            fullFace = []
            for row in range(self.magnitude):
                row = []
                for d in range(self.magnitude):
                    row.append(face)
                fullFace.append(row)
            self.state.append(fullFace)

    def equals(self, other_cube):
        return self.state == other_cube.state

    def apply_axisRotation(self, axis, modifier):
        assert(axis in Axis)
        assert(modifier in Modifier)
        if(modifier == Modifier.Twice):
            for d in range(2):
                self.apply_axisRotation(axis, Modifier.Normal)
            return
        if(modifier == Modifier.Prime):
            for d in range(3):
                self.apply_axisRotation(axis, Modifier.Normal)
            return
        assert(modifier == Modifier.Normal)
        #Need to 2D rotate Up and Down faces, and then swap/rotate respective inline faces
        if(axis == Axis.x):
            self.state[self.faces.index("R")] = rot2DArray(self.state[self.faces.index("R")])
            for rot in range(3):
                self.state[self.faces.index("L")] = rot2DArray(self.state[self.faces.index("L")])
            up = self.state[self.faces.index("U")]
            self.state[self.faces.index("U")] = self.state[self.faces.index("F")]
            self.state[self.faces.index("F")] = self.state[self.faces.index("D")]
            self.state[self.faces.index("D")] = self.state[self.faces.index("B")]
            for d in range(2):
                self.state[self.faces.index("D")] = rot2DArray(self.state[self.faces.index("D")])
            self.state[self.faces.index("B")] = up
            for d in range(2):
                self.state[self.faces.index("B")] = rot2DArray(self.state[self.faces.index("B")])
        elif(axis == Axis.y):
            self.state[self.faces.index("U")] = rot2DArray(self.state[self.faces.index("U")])
            for rot in range(3):
                self.state[self.faces.index("D")] = rot2DArray(self.state[self.faces.index("D")])
            front = self.state[self.faces.index("F")]
            self.state[self.faces.index("F")] = self.state[self.faces.index("R")]
            self.state[self.faces.index("R")] = self.state[self.faces.index("B")]
            self.state[self.faces.index("B")] = self.state[self.faces.index("L")]
            self.state[self.faces.index("L")] = front
        elif(axis == Axis.z):
            self.state[self.faces.index("F")] = rot2DArray(self.state[self.faces.index("F")])
            for rot in range(3):
                self.state[self.faces.index("B")] = rot2DArray(self.state[self.faces.index("B")])
            up = self.state[self.faces.index("U")]
            self.state[self.faces.index("U")] = self.state[self.faces.index("L")]
            self.state[self.faces.index("U")] = rot2DArray(self.state[self.faces.index("U")])
            self.state[self.faces.index("L")] = self.state[self.faces.index("D")]
            self.state[self.faces.index("L")] = rot2DArray(self.state[self.faces.index("L")])
            self.state[self.faces.index("D")] = self.state[self.faces.index("R")]
            self.state[self.faces.index("D")] = rot2DArray(self.state[self.faces.index("D")])
            self.state[self.faces.index("R")] = up
            self.state[self.faces.index("R")] = rot2DArray(self.state[self.faces.index("R")])

    def apply_move_string(self, moveString):
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

    def apply_move(self, move, modifier):
        assert(move in Move)
        assert(modifier in Modifier)
        if(modifier == Modifier.Twice):
            for d in range(2):
                self.apply_move(move, Modifier.Normal)
            return
        if(modifier == Modifier.Prime):
            for d in range(3):
                self.apply_move(move, Modifier.Normal)
            return
        if(move == Move.U):
            self.state[self.faces.index("U")] = rot2DArray(self.state[self.faces.index("U")])
            frontTopRow = self.state[self.faces.index("F")][0]
            leftTopRow = self.state[self.faces.index("L")][0]
            backTopRow = self.state[self.faces.index("B")][0]
            rightTopRow = self.state[self.faces.index("R")][0]
            self.state[self.faces.index("L")][0] = frontTopRow
            self.state[self.faces.index("B")][0] = leftTopRow
            self.state[self.faces.index("R")][0] = backTopRow
            self.state[self.faces.index("F")][0] = rightTopRow
        elif(move == Move.D):
            self.apply_axisRotation(Axis.x, Modifier.Twice)
            self.apply_move(Move.U, Modifier.Normal)
            self.apply_axisRotation(Axis.x, Modifier.Twice)
        elif(move == Move.L):
            self.apply_axisRotation(Axis.z, Modifier.Normal)
            self.apply_move(Move.U, Modifier.Normal)
            self.apply_axisRotation(Axis.z, Modifier.Prime)
        elif(move == Move.R):
            self.apply_axisRotation(Axis.z, Modifier.Prime)
            self.apply_move(Move.U, Modifier.Normal)
            self.apply_axisRotation(Axis.z, Modifier.Normal)
        elif(move == Move.F):
            self.apply_axisRotation(Axis.x, Modifier.Normal)
            self.apply_move(Move.U, Modifier.Normal)
            self.apply_axisRotation(Axis.x, Modifier.Prime)
        elif(move == Move.B):
            self.apply_axisRotation(Axis.x, Modifier.Prime)
            self.apply_move(Move.U, Modifier.Normal)
            self.apply_axisRotation(Axis.x, Modifier.Normal)

    def apply_alg(self, alg):
        moves = alg.split(" ")
        for move in moves:
            self.apply_move_string(move)

    def log(self):
        # Print Up Face
        for row in range(self.magnitude):
            for spacer in range(self.magnitude):
                print(" ", end="")
            print(" ", end="")
            for d in range(self.magnitude):
                render_face(self.state[self.faces.index("U")][row][d])
            print()
        # Print Faces Left, Front, Right, Back
        print()
        for row in range(self.magnitude):
            for d in range(self.magnitude):
                render_face(self.state[self.faces.index("L")][row][d])
            print(" ", end="")
            for d in range(self.magnitude):
                render_face(self.state[self.faces.index("F")][row][d])
            print(" ", end="")
            for d in range(self.magnitude):
                render_face(self.state[self.faces.index("R")][row][d])
            print(" ", end="")
            for d in range(self.magnitude):
                render_face(self.state[self.faces.index("B")][row][d])
            print()
        # Print Down Face
        print()
        for row in range(self.magnitude):
            for spacer in range(self.magnitude):
                print(" ", end="")
            print(" ", end="")
            for d in range(self.magnitude):
                render_face(self.state[self.faces.index("D")][row][d])
            print()