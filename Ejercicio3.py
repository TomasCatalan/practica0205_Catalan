def x(radio):
    '''Funcion que calcula el area de un circulo
    
    Parametros:
        - radio: radio del circulo
    
    Salida:
        - Entrega el area de un circulo'''

    return 3.1416 * radio**2

radio = int(input("introduzca un numero entero para el radio"))
print("el area del circulo es", x(radio))

def a(radio, altura):
    '''Funcion que calcula el area de un cilindro, 
    
    Parametros:
        - radio: radio del circulo
        - altura: altura del cilindro
    
    Salida:
        - Entrega el area de un cilindro'''
 
    c = x(radio) * altura
    return c
altura = int(input("introduzca un numero entero para la altura"))

print("el volumen del cilindro es de", a(radio, altura))

