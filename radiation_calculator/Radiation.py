class Radiation:
    """ Data class for storage dose of radiation at the point"""
    def __init__(self, x, z, rad):
        self.x = x
        self.z = z
        self.rad = rad
