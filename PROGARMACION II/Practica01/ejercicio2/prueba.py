from EcuacionLineal import EcuacionLineal

print("Ingrese a, b, c, d, e, f:")

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX())
    print("y =", ecuacion.getY())
else:
    print("La ecuación no tiene solución")
