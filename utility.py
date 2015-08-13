from __future__ import print_function
import fixpath
from colorama import *
init(autoreset=True)

# Had to rotate a 2D array 90 degrees. Rather dirty but it works
# Also had issues deepcopying the old self.state list so I did it manually
# http://stackoverflow.com/questions/16684856/rotating-a-2d-pixel-array-by-90-degrees
# Assumes array is square and not rectangular
def rot2DArray(old_array):
    magnitude = len(old_array[0])
    new_array = []
    for d in range(magnitude):
        new_array.append(old_array[d][:])
    for i in range(magnitude):
        for j in range(magnitude):
            new_array[j][magnitude - i - 1] = old_array[i][j]
    return new_array

# Standard DOS command prompt doesn't have Orange... so I had to cheat it in (Doesn't look perfect)
def render_face(face):
    backColor = Back.BLACK
    foreColor = Fore.WHITE;
    character = '\u2588'
    if(face == "U"):foreColor = Fore.WHITE
    elif(face == "D"):foreColor = Fore.YELLOW
    elif(face == "F"):foreColor = Fore.GREEN
    elif(face == "B"):foreColor = Fore.BLUE
    elif(face == "L"):
        foreColor = Fore.RED
        backColor = Back.YELLOW
        character = '\u2591'
    elif(face == "R"):foreColor = Fore.RED
    print(Style.BRIGHT + backColor + foreColor + character, end="")

def stress_test(cube, alg, iterations):
    import time
    start_time = time.time()
    for d in range(iterations):
        cube.apply_alg(alg)
    print("Took %s seconds too apply algorithm\n%s\n%i times" % ((time.time() - start_time), alg, iterations))