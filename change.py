def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    precio = input()
    print(precio)
    print("Dinero recibido")
    dinero = input()
    print(dinero)
    vuelto = int(dinero) - float(precio)
    centavos = int(vuelto*100 - int(vuelto)*100)
    pesos = int(vuelto)
    print(f"\nVuelto\n\nPesos:\n{pesos}\nCentavos:\n{centavos}")
    pass
