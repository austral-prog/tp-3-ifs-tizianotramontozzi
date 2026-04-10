def positive():
    """
    Ejercicio 1 - Clasificar Número

    Leer un número entero mediante input(). Determinar si es positivo, negativo o cero
    e imprimir el resultado correspondiente.

    Ejemplo:
        Para la entrada "5", la salida esperada es:
        El numero es positivo

        Para la entrada "-3", la salida esperada es:
        El numero es negativo

        Para la entrada "0", la salida esperada es:
        El numero es cero
    """
    pass
    numero = int(input("Ingrese un numero entero: "))

    if numero > 0 :
        print("El numero es positivo")
    elif numero < 0 :
        print("El numero es negativo")
    else:
        print("El numero es cero")

positive()