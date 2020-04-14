import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


class Visualization:

    def __init__(self):
        self.__list_of_x = list()
        self.__list_of_y = list()
        self.__list_of_z = list()

    def __make_data(self, rad_list):
        self.__list_of_x.clear()
        self.__list_of_y.clear()
        self.__list_of_z.clear()
        for item in rad_list:
            self.__list_of_x.append(item.x)
            self.__list_of_y.append(item.z)
            self.__list_of_z.append(item.N)

    def show_chart(self, rad_list):
        self.__make_data(rad_list)

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_trisurf(
            np.asarray(self.__list_of_x),
            np.asarray(self.__list_of_y),
            np.asarray(self.__list_of_z, dtype=np.float32),
            cmap=cm.rainbow,
            linewidth=0.2,
            antialiased=True
        )

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()
