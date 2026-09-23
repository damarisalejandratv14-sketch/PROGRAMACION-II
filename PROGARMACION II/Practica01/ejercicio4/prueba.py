from Estadistica import Estadistica

numeros = []

print("Ingrese 10 números:")

for i in range(10):

    numero = float(input())
    numeros.append(numero)

estadistica = Estadistica(numeros)

print("El promedio es", estadistica.promedio())

print("La desviación estándar es", estadistica.desviacion())

