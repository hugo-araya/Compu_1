altura = int(input('Altura: '))
ancho = int(input('Ancho: '))
i = 0
while i < altura:
    j = 0
    while j < ancho:
        print('*',end="")
        j = j + 1
    print()
    i = i + 1
