def lectura_datos(archivo):
    original = []
    ent = open(archivo)
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split(' ')
        original.append(lista)
    return original

def proceso(original):
    lista_salida = []
    for linea in original:
        nombre = linea[0]
        apellido = linea[1]
        ingreso = linea[2]
        salida = ingreso[2:] + nombre[0] + apellido
        lista_salida.append(salida)
    return lista_salida

def salida_datos(lista_salida):
    print('-----------------------------------')
    for elem in lista_salida:
        print('| Lo solicitado es: ', elem)
    print('-----------------------------------')

if __name__ == '__main__':
    original = lectura_datos('ejc_datos.txt')
    lista_salida = proceso(original)
    salida_datos(lista_salida)