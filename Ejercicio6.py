def decimalbinario(decimal):
    '''Funcion que transforma un numero decimal a binario
    
    Parametros:
        - x: transforma la parte entera del numero decimal introducido
        - xComa: almacena la parte decimal del numero
        - decimal: almacena el numero decimal

    Salida
        - Devuelve el numero decimal convertido a binario
        '''
    x = bin(int(decimal))[2:] #el 2: elimina el prefijo de binario (Ob)
    xComa = decimal - int(decimal)
    for i in range(int(decimal + 1)):
            xComa *= 2
            x += str(int(xComa))
            xComa -= int(xComa)
    
    print(x)
    return x

x = 45.87653
decimalbinario(x)

def binariodecimal(binario):
    '''Funcion que transforma un binario a decimal
    
    Parametros:
        - binario: se refiere al numero binario introducido en la funcion
    
    Salida:
        - devuelve el binario convertido a decimal'''

    binario = int(binario, 2) # int(num binario, 2)
    
    print(float(binario))
    return float(binario)
    
y = "10110101111010110"
binariodecimal(y)