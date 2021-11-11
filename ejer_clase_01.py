
def proceso(nombre, apellido, ingreso):
    salida = ingreso[2:] + nombre[0] + apellido
    return salida

if __name__ == '__main__':
    salida = proceso('Hugo', 'Araya', '2019')
    print('Lo solicitado es: ', salida)
