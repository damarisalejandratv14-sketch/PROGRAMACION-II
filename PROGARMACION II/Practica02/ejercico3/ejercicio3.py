import math
class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normal(self):
        len_v = self.longitud()
        if len_v == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x / len_v, self.y / len_v, self.z / len_v)

    def __add__(self, otro):
        return Vector3D(
            self.x + otro.x,
            self.y + otro.y,
            self.z + otro.z
        )

    def __mul__(self, otro):
        if isinstance(otro, (int, float)):
            return Vector3D(self.x * otro, self.y * otro, self.z * otro)
        elif isinstance(otro, Vector3D):
            return self.x * otro.x + self.y * otro.y + self.z * otro.z
        else:
            raise TypeError("Operación no soportada")

    def __rmul__(self, otro):
        return self.__mul__(otro)

    def __xor__(self, otro):
        return Vector3D(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


if __name__ == "__main__":
    a = Vector3D(1.0, 2.0, 3.0)
    b = Vector3D(4.0, 5.0, 6.0)
    print(f"Vector a: {a}")
    print(f"Vector b: {b}")
    print("-" * 35)
    suma = a + b
    print(f"Suma (a + b): {suma}")
    escalar = a * 2.0
    print(f"Escalar (a * 2): {escalar}")
    print(f"Longitud de a (|a|): {a.longitud():.4f}")
    print(f"Normal de a: {a.normal()}")
    prod_escalar = a * b
    print(f"Producto escalar (a . b): {prod_escalar}")
    prod_vectorial = a ^ b
    print(f"Producto vectorial (a x b): {prod_vectorial}")
