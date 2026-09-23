
import random
from cronometro import Cronometro

numeros = []

for i in range(1000):
    numeros.append(random.randint(0, 1000))

reloj = Cronometro()

reloj.iniciar()

for i in range(len(numeros) - 1):
    menor = i

    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[menor]:
            menor = j

    temporal = numeros[i]
    numeros[i] = numeros[menor]
    numeros[menor] = temporal

reloj.detener()

print("Tiempo de ordenamiento:", reloj.lapsoDeTiempo(), "milisegundos")

