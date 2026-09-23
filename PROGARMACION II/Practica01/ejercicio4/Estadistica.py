import math

class Estadistica:

    def __init__(self, numeros):
        self.numeros = numeros

    def promedio(self):

        suma = 0

        for numero in self.numeros:
            suma = suma + numero

        return suma / len(self.numeros)

    def desviacion(self):

        media = self.promedio()

        suma = 0

        for numero in self.numeros:
            suma = suma + (numero - media) ** 2

        return math.sqrt(suma / (len(self.numeros) - 1))

