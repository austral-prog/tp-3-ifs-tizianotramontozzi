def discount():
    """
    Ejercicio 9 (Integrador) - Sistema de Descuentos

    Crear un sistema de descuentos para una tienda. Leer mediante input():
    1. El precio unitario de un producto (decimal)
    2. La cantidad de unidades a comprar (entero)

    Calcular el total aplicando los siguientes descuentos según la cantidad:
    - Si compra 10 o más unidades: 20% de descuento
    - Si compra entre 5 y 9 unidades: 10% de descuento
    - Si compra menos de 5 unidades: sin descuento

    Imprimir:
    1. El subtotal (precio × cantidad)
    2. El porcentaje de descuento aplicado
    3. El monto del descuento
    4. El total final

    Ejemplo:
        Para las entradas "100" y "12", la salida esperada es:
        Subtotal: 1200.0
        Descuento aplicado: 20%
        Monto de descuento: 240.0
        Total final: 960.0
    """

    precio = float(input())
    cantidad = int(input())
    subtotal = precio * cantidad

    if cantidad >= 10:
        porcentaje = 20
    elif 5 <= cantidad <= 9:
        porcentaje = 10
    else:
        porcentaje = 0

    monto_descuento = (subtotal * porcentaje / 100)
    total = subtotal - monto_descuento

    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {porcentaje}%")
    print(f"Monto de descuento: {monto_descuento}")
    print(f"Total final: {total}")

discount()