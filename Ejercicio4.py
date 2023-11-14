def media():
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