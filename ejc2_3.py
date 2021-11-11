def lectura(archivo):
    ent = open(archivo)
    linea = ent.readline().rstrip('\n')
    lista = linea.split(',')
    lista1 = []
    for elem in lista:
        lista1.append(int(elem))
    return lista1

def proceso(lista):
    mayor = lista[0]
    for nro in lista:
        if nro > mayor:
            mayor = nro
    return mayor

def escritura(salida):
    print('El mayor es: ', salida)

if __name__ == '__main__':
    lista = lectura('datos_ejer2.txt')
    salida = proceso(lista)
    escritura(salida)

