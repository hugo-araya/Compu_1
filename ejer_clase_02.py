
def proceso(nombre, apellido, ingreso):
    salida = ingreso[2:] + nombre[0] + apellido
    return salida

if __name__ == '__main__':
    nombre = input('Ingrese un Nombre: ')
    apellido = input('Ingrese Apellido: ')
    ingreso = input('Agno de Ingreso: ')
    salida = proceso(nombre, apellido, ingreso)
    print('Lo solicitado es: ', salida)
