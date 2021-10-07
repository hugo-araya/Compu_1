peso = int(input('Indique su peso (en kilos): '))
estatura = float(input('Indique su estatura (en metros): '))
edad = int(input('Indique su edad (agnos): '))
cuadrado = estatura * estatura
imc = peso / cuadrado
if ((imc < 22) and (edad < 45)):
    print('Riesgo bajo')
if ((imc < 22) and (edad >= 45)):
    print('Riesgo medio')
if ((imc >= 22) and (edad < 45)):
    print('Riesgo medio')
if ((imc >= 22) and (edad >= 45)):
    print ('Riesgo alto')