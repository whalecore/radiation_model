import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from radiation_calculator import Radiation, room_radiation


for item in room_radiation(20, 28, 13, 3, 5, 6, 1, 1):
    print('x: ', item.x, 'z: ', item.z, 'N: ', item.N)
