def lectura():
    lista = [9,8,72,22,21,81,2,1,11,76,32,54,200,34,234]
    return lista

def proceso(lista):
    mayor = lista[0]
    for nro in lista:
        if nro > mayor:
            mayor = nro
    return mayor

def escritura(salida):
    print('El mayor es: ', salida)

if __name__ == '__main__':
    lista = lectura()
    salida = proceso(lista)
    escritura(salida)

