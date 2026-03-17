def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = base * altura
    perimetro = 2*base + 2*altura
    print(f"Base: {base}\nAltura: {altura}\nArea: {area}\nPerimetro: {perimetro}")
    pass



