def lectura_datos(archivo):
    ent = open(archivo)
    linea = ent.readline()
    linea = linea.rstrip('\n')
    lista = linea.split(' ')
    nombre = lista[0]
    apellido = lista[1]
    ingreso = lista[2]
    return nombre, apellido, ingreso

def proceso(nombre, apellido, ingreso):
    salida = ingreso[2:] + nombre[0] + apellido
    return salida

def salida_datos(salida):
    print('-----------------------------------')
    print('| Lo solicitado es: ', salida)
    print('-----------------------------------')

if __name__ == '__main__':
    nombre, apellido, ingreso = lectura_datos('ejc_datos.txt')
    salida = proceso(nombre, apellido, ingreso)
    salida_datos(salida)