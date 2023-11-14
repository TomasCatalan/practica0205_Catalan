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

def y(m): # BUCLE ITERATIVO
    '''Funcion que calcula el factorian de un numero entero
    con un bucle
    
    Parametros
        - n: un numero entero introducido
        
    Salida:
        - factorial del numero introducido'''
    
    for i in range(1, m + 1):
        z = z * (z -1)  
    return z
           
m = int(input("introduzca un numero entero"))
print(x(m))