from Cube_Standard import *

cube = Cube_Standard(3)
alg = "F D' B R' U D' F' L D B U2 R2 F2 D' F2 L2 B2 D' F2 D"
cube.apply_alg(alg)
cube.log()
stress_test(cube, alg, 100)