# Escriba un programa que determine si el número entero
# ingresado por el usuario  es par o no

numero1 = int(input('Ingrese un numero 1: '))
numero2 = int(input('Ingrese un numero 2: '))
resto = numero1 % numero2
if resto == 0:
    print('El numero', numero1, 'es divisible por', numero2)
else:
    print('El numero', numero1, 'NO es divisible por', numero2)

