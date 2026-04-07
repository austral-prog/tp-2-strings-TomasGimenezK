    def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = input()
    descuento = input()
    cantidad = input()
    precio_con_descuento = int(precio) - float(descuento)
    total = float(precio_con_descuento) * int(cantidad)
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_con_descuento}")
    print(f"Total: {total}")
    pass
