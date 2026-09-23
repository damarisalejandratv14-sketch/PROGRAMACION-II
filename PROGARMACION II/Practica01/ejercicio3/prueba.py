from EcuacionCuadratica import EcuacionCuadratica

print("Ingrese a, b, c:")

a = float(input())
b = float(input())
c = float(input())

ecuacion = EcuacionCuadratica(a, b, c)

discriminante = ecuacion.getDiscriminante()

if discriminante > 0:
    print("La ecuación tiene dos raíces")
    print("Raíz 1 =", ecuacion.getRaiz1())
    print("Raíz 2 =", ecuacion.getRaiz2())

elif discriminante == 0:
    print("La ecuación tiene una raíz")
    print("Raíz =", ecuacion.getRaiz1())

else:
    print("La ecuación no tiene raíces reales")
