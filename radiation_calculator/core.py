import math

from radiation_calculator.Radiation import Radiation


def __coordinate_xyz(x, y, z, x0, y0, z0):
    return (x - x0) ** 2 + (y - y0) ** 2 + (z - z0) ** 2


def __radiation_at_point(x0, y0, z0, m, l, k, n, P, R, d):
    L = 0
    for y in range(l, m):
        for z in range(l, m):
            for x in range(k, k + n):
                xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                L += __radiation_power(P, R) / (xyz * 2 ** (math.sqrt(xyz) * (x - k) / ((x - x0) * d)))
    return L


def __radiation_power(P, R):
    return P * R ** 2


def wall_radiation(k, l, m, n, y0, d, P, R):
    radiation_list = []
    for x0 in range(1, k):
        for z0 in range(1, l):
            radiation_list.append(Radiation(x0, z0, __radiation_at_point(x0, y0, z0, m, l, k, n, P, R, d)))
    return radiation_list


def room_radiation(k, l, m, n, y0, d, P, R):
    radiation_list = []
    radiation_power = __radiation_power(P, R)
    for x0 in range(1, (k - 2 * n)):
        for z0 in range(1, (l - 2 * n - 1)):
            L = 0
            for x in range(-n, (k - n)):
                for z in range(-n, (l - n)):
                    for y in range(m, m + n):
                        xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                        L += radiation_power / (xyz * 2 ** (math.sqrt(xyz) * (y - m) / ((y - y0) * d)))
                    for y in range(-n, -1):
                        xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                        L += radiation_power / (xyz * 2 ** (math.sqrt(xyz) * y / ((y - y0) * d)))
            for y in range(1, m):
                for z in range(1, l - 2 * n):
                    for x in range(k - 2 * n, k - n):
                        xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                        L += radiation_power / (xyz * 2 ** (math.sqrt(xyz) * (x - k + 2 * n) / ((x - x0) * d)))
                    for x in range(-n, -1):
                        xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                        L += radiation_power / (xyz * 2 ** (math.sqrt(xyz) * x / ((x - x0) * d)))
            for x in range(-n, k - n):
                for y in range(1, m):
                    for z in range(-n, -1):
                        xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                        L += radiation_power / (xyz * 2 ** (math.sqrt(xyz) * z / ((z - z0) * d)))
                    for z in range(l - 2 * n, l - n):
                        xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                        L += radiation_power / (xyz * 2 ** (math.sqrt(xyz) * (z - 1 + 2 * n) / ((z - z0) * d)))
            radiation_list.append(Radiation(x0, z0, L))
    return radiation_list
