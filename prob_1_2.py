# Determina si un numero es primo

numero = int(input("Ingrese un numero : "))
nro = 2
status = True
while nro < numero-1:
    print(nro)
    resto = numero % nro
    if resto == 0:
        status = False
    nro = nro + 1
if status == True:
    print('El numero', numero,'es PRIMO')
else:
    print('El numero', numero,'NO es PRIMO')

