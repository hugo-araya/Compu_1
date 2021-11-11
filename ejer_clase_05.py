def lectura_datos(nombre_archivo):
    todos = []
    ent = open(nombre_archivo)
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split(' ')
        todos.append(lista)
    return todos

def proceso(todos):
    solicitado = []
    for elem in todos:
        nombre = elem[0]
        apellido = elem[1]
        ingreso = elem[2]
        salida = ingreso[2:] + nombre[0] + apellido
        solicitado.append(salida)
    return solicitado

def salida_datos(solicitado):
    print('--------------------------------------')
    for elem in solicitado:
        print('- Lo solicitado es: ', elem)
    print('--------------------------------------')

if __name__ == '__main__':
    todos = lectura_datos('datos_ejer.txt')
    solicitado = proceso(todos)
    salida_datos(solicitado)
