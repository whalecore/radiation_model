import os
import sys
from radiation_calculator import room_radiation, Visualization, IncorrectValues

try:
    rad_list = room_radiation(28, 20, 13, 1, 5, 3, 1, 1)

    for item in rad_list:
        print('x: ', item.x, 'z: ', item.z, 'N: ', item.rad)

    visual = Visualization()
    visual.show_chart(rad_list)
except IncorrectValues as e:
    print(e.message)
