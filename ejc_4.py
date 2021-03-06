def lectura_datos(archivo):
    ent = open(archivo)
    nombre = ent.readline()
    nombre = nombre.rstrip('\n')
    apellido = ent.readline()
    apellido = apellido.rstrip('\n')
    ingreso = ent.readline()
    ingreso = ingreso.rstrip('\n')
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