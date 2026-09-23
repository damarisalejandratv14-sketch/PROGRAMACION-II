import time

class Cronometro:

    def __init__(self):
        self.inicia = 0
        self.finaliza = 0

    def iniciar(self):
        self.inicia = time.time() * 1000

    def detener(self):
        self.finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        return self.finaliza - self.inicia

    def getInicia(self):
        return self.inicia

    def getFinaliza(self):
        return self.finaliza
