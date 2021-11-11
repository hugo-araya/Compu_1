def proceso(nombre, apellido, ingreso):
    salida = ingreso[2:] + nombre[0] + apellido
    return salida

if __name__ == '__main__':
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    ingreso = input('Ingreso: ')
    salida = proceso(nombre, apellido, ingreso)
    print('Lo solicitado es: ', salida)