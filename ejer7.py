print("Evaluación Crediticia")
nom= input("Nombre: ")
edad= int(input("Edad: "))
ingre= int(input("Ingreso mensual: "))
egre= int(input("Egreso mensual: "))
cant= int(input("Cantidad del prestamo a solicitar: "))
mes= int(input("Meses a pagar: "))

total=ingre-egre
cuota=cant/mes

if edad < 18 or ingre < egre or total < cuota:
    print("No cumple con los requisitos para obtener el crédito")
else :
    print("Cumple con los requisitos para obtener el crédito")