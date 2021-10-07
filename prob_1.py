# Escriba un programa que determine si el número 
# entero ingresado por el usuario es par o no.

numero = int(input("Ingrese un numero: "))
resto = numero % 2
if resto == 0:
    print('Es PAR')
else:
    print('NO es PAR')
