# Radiation Model library
A little library for modelling radiation inside buildings
***
## Install:
Clone the repo and run setup.py. This lib needs matplotlib to work properly.
***
## 1. Calculating radiation background from a wall

* wall_radiation method:
    A method for calculating radiation background from a wall,
    which should be perpendicular to the x axis and parallel
    to the z axis. This method returns a list of radiation doses in each point
    of the y0 plane. It takes 8 parameters:

    1. k: int, defines x-axis distance from the wall
    2. l: int, defines z-axis wall size
    3. m: int, defines y-axis wall size
    4. n: int, defines x-axis wall size
    5. y0: int, a distance to the plane along the y axis
    6. d: int, a half attenuation thickness (constant dependent on wall material)
    7. p: int, default = 1, the value of the radiation power at distance r from a single element
    8. r: int, default = 1, a distance from a single element of wall

## 2. Calculating radiation background in a room

* room_radiation method:
 A method for calculating radiation background in a room.
    All parameters are relative to the wall, which is perpendicular to the axis x
    and parallel to the axis z. This method returns a list of radiation doses in each point of the y0 plane.
    It takes 8 parameters:
    1. k: int, x-axis distance from the wall
    2. l: int, z-axis wall size
    3. m: int, y-axis wall size
    4. n: int, x-axis wall size
    5. y0: int, distance to the plant along the y axis
    6. d: int, half attenuation thickness (constant dependent on wall material)
    7. p: int, the value of the radiation power at distance r from a single element
    8. r: int, distance from a single element of a wall

## 3. Visualization
* show_chart method:
 Visualization class' method that builds a 3D graph of radiation levels in a room. It takes a list made with wall_radiation or room_radiation methods