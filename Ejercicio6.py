def decimalbinario(decimal):

    x = bin(int(decimal))[2:]
    xComa = decimal - int(decimal)
    for _ in range(int(decimal + 1)):
            xComa *= 2
            x += str(int(xComa))
            xComa -= int(xComa)
    
    print(x)
    return x

x= 45.89763
decimalbinario(x)