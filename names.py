def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    print(nombre.lower()+ " " + apellido.lower())
    print(nombre.title() + " " + apellido.title())
    print(nombre.upper() + " " + apellido.upper())
    print("\t" + nombre.lower() + " " + apellido.lower())
    pass


