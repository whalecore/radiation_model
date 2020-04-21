import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from radiation_calculator import wall_radiation, Visualization

rad_list = wall_radiation(28, 20, 13, 1, 5, 6, 1, 1)

for item in rad_list:
    print('x: ', item.x, 'z: ', item.z, 'N: ', item.rad)

visual = Visualization()
visual.show_chart(rad_list)
