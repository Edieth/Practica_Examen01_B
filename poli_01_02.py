# --------------------------------------------------
# Creates main class
# --------------------------------------------------
import math
class Geometria:
    def __init__(self, valores):
        self.valores = valores

    def area(self):
        pass

    def formula(self):
        pass

    def datos(self):
        pass


# --------------------------------------------------
# Creates derived classes with abstract methods
# --------------------------------------------------
class cuadrado(Geometria):
    def area(self):
        return self.valores[0] ** 2

    def formula(self):
        return 'Base * Base'

    def datos(self):
        return self.valores[0]


class rectangulo(Geometria):
    def area(self):
        return self.valores[0] * self.valores[1]

    def formula(self):
        return 'Base * Altura'

    def datos(self):
        return str(self.valores[0]) + ', ' + str(self.valores[1])

class triangulo (Geometria):
#triangulo equilátero
    def area_eq(self):
       return (math.sqrt(3) / 4) * self.valores[0] ** 2

    def formula_eq(self):
        return 'Raíz (3)/4* (Lado)^2'

    def datos_eq(self):
        return str(self.valores[0]) + ' : es el valor de todos los lados'

#triangulo isóceles
    def area_iso(self):
        return (self.valores[0] * self.valores[1])/2

    def formula_iso(self):
        return 'Base*Altura/2'

    def datos_iso(self):
        return str(self.valores[0]) + ', ' + str(self.valores[1])

#triangulo escaleno
    def area_escaleno(self):
        s = (self.valores[0] +self.valores[1] + self.valores[2]) / 2
        return math.sqrt(s * (s -self.valores[0] ) * (s -self.valores[1] ) * (s -self.valores[2] ))

    def formula_escaleno(self):
        return 'semi perimetro S = (a+b+c)/2 y el área es: Raíz (S*(S-a)*(S-b)*(S-c)) donde a, b y c son los lados'

    def datos_escaleno(self):
        return str(self.valores[0]) + ', ' + str(self.valores[1]) + ', ' + str(self.valores[2])
# --------------------------------------------------
# Using classes
# --------------------------------------------------
fig1 = cuadrado([3])
print('La formula del cuadrado es {0}.'.format(fig1.formula()))
print('Y con la siguiente lista de valores [{0}] obtenemos un área de {1}'.format(fig1.datos(), fig1.area()))

print()

fig2 = rectangulo([3, 5])
print('La formula del rectángulo es {0}.'.format(fig2.formula()))
print('Y con la siguiente lista de valores [{0}] obtenemos un área de {1}'.format(fig2.datos(), fig2.area()))

print()

fig3 = triangulo([5])
print('La formula del triángulo equilátero es {0}.'.format(fig3.formula_eq()))
print('Y con la siguiente lista de valores [{0}] obtenemos un área de {1}'.format(fig3.datos_eq(), fig3.area_eq()))

print()

fig3 = triangulo([5,8])
print('La formula del triángulo isoceles es {0}.'.format(fig3.formula_iso()))
print('Y con la siguiente lista de valores [{0}] obtenemos un área de {1}'.format(fig3.datos_iso(), fig3.area_iso()))

print()

fig3 = triangulo([10,8,6])
print('La formula del triángulo escaleno es {0}.'.format(fig3.formula_escaleno()))
print('Y con la siguiente lista de valores [{0}] obtenemos un área de {1}'.format(fig3.datos_escaleno(), fig3.area_escaleno()))
