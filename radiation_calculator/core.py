import math

from radiation_calculator.exceptions import IncorrectValues
from radiation_calculator.Radiation import Radiation
from radiation_calculator.utils import interval


def __coordinate_xyz(x, y, z, x0, y0, z0):
    """Method for calculating location relative to the origin coordinate"""
    return ((x - x0) ** 2) + ((y - y0) ** 2) + ((z - z0) ** 2)


def __radiation_at_point(x0, y0, z0, m, l, k, n, p, r, d):
    """Method for calculating dose of radiation at point"""
    rad = 0
    radiation_power = __radiation_power(p, r)
    for y in interval(1, m):
        for z in interval(1, l):
            for x in interval(k, k + n):
                xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                c = math.sqrt(xyz) * (x - k) / (x - x0)
                rad += radiation_power / (xyz * 2**(c / d))
    return rad


def __radiation_power(p, r):
    """Method for calculating radiation power from a single element of wall"""
    return p * r ** 2


def wall_radiation(k, l, m, n, y0, d, p=1, r=1):
    """Method for calculating radiation background from the radioactive wall.
    Wall perpendicular to the x axis and parallel to the z axis.

    Parameters
    ----------

    :param k: x-axis distance from the wall
    :type k: int

    :param l: z-axis wall size
    :type l: int

    :param m: y-axis wall size
    :type m: int

    :param n: x-axis wall size
    :type n: int

    :param y0: distance to the plane along the y axis
    :type y0: int

    :param d: half attenuation thickness (constant dependent on wall material)
    :type d: int

    :param p: the value of the radiation power at distance r from a single element
    :type p: int

    :param r: distance from a single element of wall
    :type r: int

    :return Dose of radiation in each point of the y0 plane
    :rtype List[Radiation]

    """
    try:
        radiation_list = []
        for x0 in interval(1, k - 1):
            for z0 in interval(1, l - 1):
                rap = __radiation_at_point(x0, y0, z0, m, l, k, n, p, r, d)
                radiation_list.append(Radiation(x0, z0, rap))
        return radiation_list
    except ZeroDivisionError:
        raise IncorrectValues('Переданы некорректные значения')


def room_radiation(k, l, m, n, y0, d, p, r):
    """Method for calculating radiation background from the radioactive room.
        Parameters are relative to the wall, which is perpendicular to the axis x and parallel to the axis z.

        Parameters
        ----------

        :param k: x-axis distance from the wall
        :type k: int

        :param l: z-axis wall size
        :type l: int

        :param m: y-axis wall size
        :type m: int

        :param n: x-axis wall size
        :type n: int

        :param y0: distance to the plane along the y axis
        :type y0: int

        :param d: half attenuation thickness (constant dependent on wall material)
        :type d: int

        :param p: the value of the radiation power at distance r from a single element
        :type p: int

        :param r: distance from a single element of wall
        :type r: int

        :return Dose of radiation in each point of the y0 plane
        :rtype List[Radiation]

    """
    validate(k, l, m, n, y0, d, p, r)
    try:
        radiation_list = []
        radiation_power = __radiation_power(p, r)
        for x0 in interval(1, (k - 2 * n - 1)):
            for z0 in interval(1, (l - 2 * n - 1)):
                rad = 0
                for x in interval(-n, (k - n)):
                    for z in interval(-n, (l - n)):
                        for y in interval(m, m + n):
                            xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                            if xyz == 0:
                                raise IncorrectValues('x не должно быть равно x0, y не должно быть равно y0, z не должно быть равно z0 одновременно')
                            if y == y0:
                                raise IncorrectValues('y не должно быть равно y0')
                            rad += radiation_power / (xyz * 2 ** ((math.sqrt(xyz) * (y - m)) / ((y - y0) * d)))
                        for y in interval(-n, -1):
                            xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                            if xyz == 0:
                                raise IncorrectValues('x не должно быть равно x0, y не должно быть равно y0, z не должно быть равно z0 одновременно')
                            if y == y0:
                                raise IncorrectValues('y не должно быть равно y0')
                            rad += radiation_power / (xyz * 2 ** ((math.sqrt(xyz) * y) / ((y - y0) * d)))
                for y in interval(l, m):  # Сюда никогда не зайдёт если l > m
                    for z in interval(l, l - 2 * n):  # Какой-то сакральный смысл у этого цикла? в него никогда не зайдёт, l всегда больше l - 2 * n. Цикл выше, не работающий в половине случаев тоже бессмысленный получается
                        for x in interval(k - 2 * n, k - n):
                            xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                            if xyz == 0:
                                raise IncorrectValues('x не должно быть равно x0, y не должно быть равно y0, z не должно быть равно z0 одновременно')
                            if y == y0:
                                raise IncorrectValues('x не должно быть равно x0')
                            rad += radiation_power / (xyz * 2 ** ((math.sqrt(xyz) * (x - k + 2 * n)) / ((x - x0) * d)))
                        for x in interval(-n, -1):
                            xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                            if xyz == 0:
                                raise IncorrectValues('x не должно быть равно x0, y не должно быть равно y0, z не должно быть равно z0 одновременно')
                            if y == y0:
                                raise IncorrectValues('x не должно быть равно x0')
                            rad += radiation_power / (xyz * 2 ** ((math.sqrt(xyz) * x) / ((x - x0) * d)))
                for x in interval(-n, k - n):
                    for y in interval(l, m):  # Сюда никогда не зайдёт если l > m
                        for z in interval(-n, -1):
                            xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                            if xyz == 0:
                                raise IncorrectValues('x не должно быть равно x0, y не должно быть равно y0, z не должно быть равно z0 одновременно')
                            if y == y0:
                                raise IncorrectValues('z не должно быть равно z0')
                            rad += radiation_power / (xyz * 2 ** ((math.sqrt(xyz) * z) / ((z - z0) * d)))
                        for z in interval(l - 2 * n, l - n):
                            xyz = __coordinate_xyz(x, y, z, x0, y0, z0)
                            if xyz == 0:
                                raise IncorrectValues('x не должно быть равно x0, y не должно быть равно y0, z не должно быть равно z0 одновременно')
                            if y == y0:
                                raise IncorrectValues('z не должно быть равно z0')
                            rad += radiation_power / (xyz * 2 ** ((math.sqrt(xyz) * (z - l + 2 * n)) / ((z - z0) * d)))
                radiation_list.append(Radiation(x0, z0, rad))
        return radiation_list
    except ZeroDivisionError:
        raise IncorrectValues('Некорректные значения')


def validate(k, l, m, n, y0, d, p, r):
    if k < 0:
        raise IncorrectValues('k не должно быть меньше 0')
    if l <= 0:
        raise IncorrectValues('l должно быть больше 0')
    if m <= 0:
        raise IncorrectValues('m должно быть больше 0')
    if n <= 0:
        raise IncorrectValues('n должно быть больше 0')
    if y0 < 0:
        raise IncorrectValues('y0 не должно быть меньше 0')
    if d <= 0:
        raise IncorrectValues('d должно быть больше 0')
    if p < 0:
        raise IncorrectValues('p не должно быть меньше 0')
    if r < 0:
        raise IncorrectValues('r не должно быть меньше 0')
    if n > k / 2 - 1:
        raise IncorrectValues('Верхняя граница n равна k / 2 - 1')
    if n > l / 2 - 1:
        raise IncorrectValues('Верхняя граница n равна l / 2 - 1')

