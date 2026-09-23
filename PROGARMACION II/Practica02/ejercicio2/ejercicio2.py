import math
class AlgebraVectorial:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def pp(self, v):
        return self.x * v.x + self.y * v.y

    def mod(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def per(self, v, op=1):

        if op == 1:
            sx = self.x + v.x
            sy = self.y + v.y
            rx = self.x - v.x
            ry = self.y - v.y
            s = math.sqrt(sx ** 2 + sy ** 2)
            r = math.sqrt(rx ** 2 + ry ** 2)
            return abs(s - r) < 0.0001

        elif op == 2:
            x1 = self.x - v.x
            y1 = self.y - v.y
            x2 = v.x - self.x
            y2 = v.y - self.y
            r1 = math.sqrt(x1 ** 2 + y1 ** 2)
            r2 = math.sqrt(x2 ** 2 + y2 ** 2)

            return abs(r1 - r2) < 0.0001

        elif op == 3:
            return self.pp(v) == 0

        elif op == 4:
            sx = self.x + v.x
            sy = self.y + v.y
            iz = sx ** 2 + sy ** 2
            de = self.mod() ** 2 + v.mod() ** 2
            return abs(iz - de) < 0.0001

    def par(self, v, op=1):
        if op == 1:
            if v.x != 0:
                r = self.x / v.x
                return abs(self.y - r * v.y) < 0.0001
            elif v.y != 0:
                r = self.y / v.y
                return abs(self.x - r * v.x) < 0.0001
            else:
                return False
        elif op == 2:
            cr = self.x * v.y - self.y * v.x
            return cr == 0

    def proy(self, v):
        p = self.pp(v)
        m = v.mod()
        if m == 0:
            return "No se puede proyectar"
        f = p / (m ** 2)
        x = f * v.x
        y = f * v.y
        return AlgebraVectorial(x, y)

    def comp(self, v):
        p = self.pp(v)
        m = v.mod()
        if m == 0:
            return "No se puede calcular"
        return p / m


a = AlgebraVectorial(2, 3)
b = AlgebraVectorial(4, 6)
print("Vector a:", a.x, a.y)
print("Vector b:", b.x, b.y)
print("\nPERPENDICULAR")
print("a)", a.per(b, 1))
print("b)", a.per(b, 2))
print("c)", a.per(b, 3))
print("d)", a.per(b, 4))
print("\nPARALELA")
print("e)", a.par(b, 1))
print("f)", a.par(b, 2))
print("\nPROYECCION")
p = a.proy(b)
if isinstance(p, AlgebraVectorial):
    print("Proyección:", p.x, p.y)
else:
    print(p)
print("\nCOMPONENTE")
print("Componente:", a.comp(b))
