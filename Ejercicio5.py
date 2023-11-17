def cuadrado():
    '''Funcion que calcula los cuadrados de una lista
    
    Parametros:
        - no tiene, al iniciar preguntara por un numero,
        introducir cualquier otra cosa que no sea float, para terminar
        
    Solucion:
        - el programa entregara el cuadrado de los numeros introducidos 
        en el diccionario, en el orden que fueron introducidos'''
    
    x = []
    while True:
       try:
            y = float(input("introduce un numero, otra cosa para terminar"))
            x.append(y)
       except ValueError:
           break
    
    if x:
        z = [a**2 for a in x]
        print("los cuadrados de", x, "son igual a",z)
    return

cuadrado()