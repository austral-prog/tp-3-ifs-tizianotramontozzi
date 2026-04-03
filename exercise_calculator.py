def calculator():
    """
    Ejercicio 7 - Calculadora Simple

    Leer dos números (pueden ser decimales) y una operación (+, -, *, /) mediante input().
    Realizar la operación correspondiente e imprimir el resultado.

    Validaciones:
    - Si la operación es inválida, imprimir "Operacion invalida"
    - Si es división y el divisor es cero, imprimir "Error: division por cero"

    Ejemplo:
        Para las entradas "10", "5" y "+", la salida esperada es:
        Resultado: 15.0

        Para las entradas "10", "2" y "/", la salida esperada es:
        Resultado: 5.0

        Para las entradas "10", "0" y "/", la salida esperada es:
        Error: division por cero

        Para las entradas "10", "5" y "x", la salida esperada es:
        Operacion invalida
    """

    num1 = float(input())
    num2 = float(input())
    op = input()

    if op == "+":
        print(f"Resultado: {num1 + num2}")
    elif op == "-":
        print(f"Resultado: {num1 - num2}")
    elif op == "*":
        print(f"Resultado: {num1 * num2}")
    elif op == "/":
        if num2 == 0:
            print("Error: division por cero")
        else :
            print(f"Resultado: {num1 / num2}")
    else:
        print("Operacion invalida")

calculator()