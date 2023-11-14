def x(y):

    return 3.1416 * y**2

y = int(input("introduzca un numero entero para el radio"))
print("el area del circulo es", x(y))

def a(y, b):

    d = x(y)
    c = d * b
    return c
b = int(input("introduzca un numero entero para la altura"))

print("el volumen del cilindro es de", a(y, b))

