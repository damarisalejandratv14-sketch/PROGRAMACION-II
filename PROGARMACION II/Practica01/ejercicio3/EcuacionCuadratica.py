import math

class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b ** 2 - 4 * self.a * self.c

    def getRaiz1(self):
        discriminante = self.getDiscriminante()

        if discriminante < 0:
            return 0

        return (-self.b + math.sqrt(discriminante)) / (2 * self.a)

    def getRaiz2(self):
        discriminante = self.getDiscriminante()

        if discriminante < 0:
            return 0

        return (-self.b - math.sqrt(discriminante)) / (2 * self.a)
