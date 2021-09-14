res1 = float(input("Ingrese el valor de la primera resistencia: "))
res2 = float(input("Ingrese el valor de la segunda resistencia: "))

total=(res1*res2)/(res1+res2)
print("El valor de la resistencia total en paralelo es: " + str(total)+ " ohms.")