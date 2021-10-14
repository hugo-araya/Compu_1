import math
final = int(input('Numero: '))
exponente = 0
while exponente <= final:
    print('2 ^', exponente,'=',int(math.pow(2, exponente)))
    exponente = exponente + 1
