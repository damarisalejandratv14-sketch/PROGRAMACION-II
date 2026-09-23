import math
class MiPunto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distancia(self, punto, y=None):
        if isinstance(punto, MiPunto):
            x2 = punto.x
            y2 = punto.y
        else:
            x2 = punto
            y2 = y

        distancia = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        return distancia
p1 = MiPunto()
p2 = MiPunto(10, 30.5)
d = p1.distancia(p2)
print("Punto 1:", p1.getX(), p1.getY())
print("Punto 2:", p2.getX(), p2.getY())
print("Distancia:", d)
