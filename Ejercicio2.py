def x(n): # FUNCION RECURSIVA
    '''Funcion que calcula el factorial de un numero entero
    
    Parametros:
        - n: un numero entero introducido
    Salida: 
        - factorial del numero introducido'''

    if n == 0:
        return 1
    else:
        return n * x(n - 1)
    
n = int(input("introduzca un numero entero"))
print(x(n))

def y(m):
    for i in range(1, m + 1):
        
    
m = int(input("introduzca un numero entero"))