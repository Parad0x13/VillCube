class Cube:
    def __init__(self, magnitude=3):
        self.magnitude = magnitude
        self.reset()

    def equals(self, other_cube):
        raise NotImplementedError

    def apply_move(self, move):
        raise NotImplementedError

    def apply_alg(self, alg):
        raise NotImplementedError

    def log(self):
        raise NotImplementedError
