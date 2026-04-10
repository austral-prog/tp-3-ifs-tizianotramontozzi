def weekday():
    """
    Ejercicio 6 - Día Hábil

    Leer un día de la semana mediante input() (en minúsculas: lunes, martes, etc.).
    Determinar si es un día hábil o fin de semana.

    Un día es hábil si NO es sábado y NO es domingo (usar operador not).

    Ejemplo:
        Para la entrada "lunes", la salida esperada es:
        Dia habil

        Para la entrada "sabado", la salida esperada es:
        Fin de semana

        Para la entrada "domingo", la salida esperada es:
        Fin de semana
    """

    dia = input("Ingrese el dia de la semana: ").lower()

    if dia == "sabado" or dia == "domingo":
        print("Fin de semana")
    else:
        print("Dia habil")