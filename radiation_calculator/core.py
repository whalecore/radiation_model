import math

class RadiationCalculator:

    def __init__(self, x, z, N, radiation_list=None):
        self.x = x
        self. z = z
        self.N = N
        if radiation_list is None:
           self.radiation_list = [20, 28, 13, 1, 5, 6, 1, 1]

    def coordinate_xyz(self, x, y, z, x0, y0, z0):
        return (x - x0) * 2 + (y - y0) * 2 + (z - z0) * 2

    def radiation_at_point(self, x0, y0, z0, m, l, k, n, P, R, d):
        L = 0
        for y in range(l, m):
            for z in range(l, m):
                for x in range(k, k+n):
                    xyz = self.coordinate_xyz(x, y, z, x0, y0, z0)
                    L += (P * R**n) / (xyz * 2**math.sqrt(xyz) * (x - k)) / ((x - x0) * d)
        return L

    def rad_calc(self, k, l, m, n, y0, d, P, R):
        radiation_list = []
        for x0 in range(l, k):
            for z0 in range(1, l):
                radiation_list.append(RadiationCalculator(x0, z0, self.radiation_at_point(x0, y0, z0, m, l, k, n, P, R, d)))
        return radiation_list