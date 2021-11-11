def proceso(lista):
    mayor = lista[0]
    for nro in lista:
        if nro > mayor:
            mayor = nro
    return mayor

if __name__ == '__main__':
    lista = [9,8,72,22,21,81,2,101,11,76,32,54]
    salida = proceso(lista)
    print ('El mayor es: ', salida)
