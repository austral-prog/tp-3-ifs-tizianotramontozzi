def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    pass
    clave = input()
    largo = len(clave) >= 8
    numero = ("0" in clave or "1" in clave or "2" in clave or "3" in clave or "4" in clave or "5" in clave or "6" in clave or "7" in clave or "8" in clave or "9" in clave)

    if largo and numero:
        print("Contraseña valida")
    else:
        if not largo:
            print("Contraseña muy corta")
        if not numero:
            print("Debe contener un numero")

password()