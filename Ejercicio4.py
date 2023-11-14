def media():
    '''Funcion que calcula la media
    
    Parametros:
        - no tiene, al iniciar preguntara por un numero,
        introducir cualquier otra cosa que no sea float, para terminar
        
    Solucion:
        - el programa entregara la media de los numeros introducidos 
        en el diccionario'''
    
    x = []
    while True:
       try:
            y = float(input("introduce un numero, otra cosa para terminar"))
            x.append(y)
       except ValueError:
           break
    
    if x:
        z = sum(x) / len(x)
        print("la media de", x, "es igual a",z)

media()