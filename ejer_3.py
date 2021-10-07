a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))

if a < (b + c):
    if b < (a + c):
        if c < (a + b):
            print ('Triangulo es valido')
            if (a == b) and (b == c):
                print ('Triangulo equilatero')
            else:
                if ((a == b) and (a == c)) or ((b == c) and (b == a)):
                    print('Triangulo Isoceles')
                else:
                    print('Triangulo Escaleno')
        else:
            print ('Triangulo NO valido')
    else:
        print ('Triangulo NO valido')
else:
    print ('Triangulo NO valido')

