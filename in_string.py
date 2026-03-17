def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    nombre = input("Ingrese nombre: ").lower()
    a = str("a" in nombre)
    e = str("e" in nombre)
    i = str("i" in nombre)
    o = str("o" in nombre)
    u = str("u" in nombre)
    print("Contiene a: " + a)
    print("Contiene e: " + e)
    print("Contiene i: " + i)
    print("Contiene o: " + o)
    print("Contiene u: " + u)

    pass

