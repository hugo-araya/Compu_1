def lectura_datos():
    nombre = input('Ingrese un Nombre: ')
    apellido = input('Ingrese Apellido: ')
    ingreso = input('Agno de Ingreso: ')
    return nombre, apellido, ingreso

def proceso(nombre, apellido, ingreso):
    salida = ingreso[2:] + nombre[0] + apellido
    return salida

def salida_datos(salida):
    print('--------------------------------------')
    print('- Lo solicitado es: ', salida)
    print('--------------------------------------')

if __name__ == '__main__':
    nombre, apellido, ingreso = lectura_datos()
    salida = proceso(nombre, apellido, ingreso)
    salida_datos(salida)
