def x(factorialrecursivo): # FUNCION RECURSIVA
    '''Funcion que calcula el factorial de un numero entero
    
    Parametros:
        - n: un numero entero introducido
    Salida: 
        - factorial del numero introducido'''

    if factorialrecursivo == 0:
        return 1
    else:
        return factorialrecursivo * x(factorialrecursivo - 1)
    
factorialrecursivo = int(input("introduzca un numero entero"))
print(x(factorialrecursivo))

def y(factorialiterativo): # BUCLE ITERATIVO
    '''Funcion que calcula el factorian de un numero entero
    con un bucle
    
    Parametros
        - n: un numero entero introducido
        
    Salida:
        - factorial del numero introducido'''
    
    for i in range(1, factorialiterativo + 1):
        z = z * (z -1)  
    return z
           
factorialiterativo = int(input("introduzca un numero entero"))
print(x(factorialiterativo))