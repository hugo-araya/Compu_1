# Escriba un programa que reciba como entrada dos números, 
# y los muestre ordenados de menor a mayor:

numero1 = int(input('Primer numero: '))
numero2 = int(input('Segundo numero: '))
if numero1 < numero2:
    print(numero1, numero2)
else:
    print(numero2, numero1)
