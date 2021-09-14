from math import sqrt
a = float(input("Ingrese coeficiente de x^2: "))
b = float(input("Ingrese coeficiente de x: "))
c = float(input("Ingrese coeficiente de variable: "))
x1=0
x2=0
if ((b**2)-4*a*c) < 0:
    print("La solucion son números complejos")
else:
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print("Las soluciones son: ")
    print(x1)
    print(x2)