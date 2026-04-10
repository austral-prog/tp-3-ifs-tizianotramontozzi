# TP3 - Trabajo Práctico 3

## Temas evaluados

Condicionales (if, if-else, if-elif-else), operadores de comparación, operadores lógicos (and, or, not), variables booleanas.

## Cómo ejecutar los tests

Para verificar todos los ejercicios:

```bash
pytest
```

Para verificar un ejercicio en particular:

```bash
pytest test_tp3_positive.py
```

---

## Ejercicios

### Ejercicio 1 — `exercise_positive.py`

**Archivo de test:** `test_tp3_positive.py`

**Conceptos:** `input()`, `int()`, `if-elif-else`, operadores de comparación (`>`, `<`, `==`).

**Consigna:** Leer un número entero mediante `input()`. Determinar si es positivo, negativo o cero e imprimir el resultado correspondiente.

**Ejemplo:** Para la entrada `"5"`, la salida esperada es:

```
El numero es positivo
```

Para la entrada `"-3"`, la salida esperada es:

```
El numero es negativo
```

Para la entrada `"0"`, la salida esperada es:

```
El numero es cero
```

---

### Ejercicio 2 — `exercise_even_odd.py`

**Archivo de test:** `test_tp3_even_odd.py`

**Conceptos:** `input()`, `int()`, `if-else`, operador `%` (módulo).

**Consigna:** Leer un número entero mediante `input()`. Determinar si el número es par o impar e imprimir el resultado correspondiente.

**Ejemplo:** Para la entrada `"8"`, la salida esperada es:

```
El numero 8 es par
```

Para la entrada `"7"`, la salida esperada es:

```
El numero 7 es impar
```

---

### Ejercicio 3 — `exercise_age_check.py`

**Archivo de test:** `test_tp3_age_check.py`

**Conceptos:** `input()`, `int()`, `if-elif-else`, operadores de comparación, validación de entrada.

**Consigna:** Leer una edad y un límite de edad mediante `input()`. Verificar que ambos números sean válidos (positivos), y luego determinar si la persona es mayor de edad comparando con el límite ingresado. Si alguno de los números es negativo o cero, imprimir `"Entrada invalida"`.

**Ejemplo:** Para las entradas `"20"` y `"18"`, la salida esperada es:

```
Eres mayor de edad
```

Para las entradas `"16"` y `"18"`, la salida esperada es:

```
Eres menor de edad
```

Para las entradas `"-5"` y `"18"`, la salida esperada es:

```
Entrada invalida
```

---

### Ejercicio 4 — `exercise_compare.py`

**Archivo de test:** `test_tp3_compare.py`

**Conceptos:** `input()`, `int()`, `if-elif-else`, operadores de comparación (`>`, `<`, `==`).

**Consigna:** Leer dos números enteros mediante `input()`. Compararlos e imprimir si el primero es mayor, menor o igual al segundo.

**Ejemplo:** Para las entradas `"10"` y `"5"`, la salida esperada es:

```
10 es mayor que 5
```

Para las entradas `"3"` y `"8"`, la salida esperada es:

```
3 es menor que 8
```

Para las entradas `"7"` y `"7"`, la salida esperada es:

```
7 es igual a 7
```

---

### Ejercicio 5 — `exercise_grades.py`

**Archivo de test:** `test_tp3_grades.py`

**Conceptos:** `input()`, `int()`, `if-elif-else`, múltiples rangos de comparación.

**Consigna:** Leer una nota (0-10) mediante `input()`. Clasificar la nota e imprimir:
- `"Excelente"` si está entre 9 y 10
- `"Bueno"` si está entre 7 y 8
- `"Regular"` si está entre 5 y 6
- `"Insuficiente"` si está entre 0 y 4

**Ejemplo:** Para la entrada `"9"`, la salida esperada es:

```
Excelente
```

Para la entrada `"6"`, la salida esperada es:

```
Regular
```

Para la entrada `"3"`, la salida esperada es:

```
Insuficiente
```

---

### Ejercicio 6 — `exercise_weekday.py`

**Archivo de test:** `test_tp3_weekday.py`

**Conceptos:** `input()`, operador lógico `not`, `if-else`, comparación de strings.

**Consigna:** Leer un día de la semana mediante `input()` (en minúsculas: lunes, martes, etc.). Determinar si es un día hábil o fin de semana. Un día es hábil si NO es sábado y NO es domingo (usar operador `not`).

**Ejemplo:** Para la entrada `"lunes"`, la salida esperada es:

```
Dia habil
```

Para la entrada `"sabado"`, la salida esperada es:

```
Fin de semana
```

Para la entrada `"domingo"`, la salida esperada es:

```
Fin de semana
```

---

### Ejercicio 7 — `exercise_calculator.py`

**Archivo de test:** `test_tp3_calculator.py`

**Conceptos:** `input()`, `float()`, `if-elif-else`, operaciones matemáticas, comparación de strings, validación.

**Consigna:** Leer dos números (pueden ser decimales) y una operación (`+`, `-`, `*`, `/`) mediante `input()`. Realizar la operación correspondiente e imprimir el resultado.

Validaciones:
- Si la operación es inválida, imprimir `"Operacion invalida"`
- Si es división y el divisor es cero, imprimir `"Error: division por cero"`

**Ejemplo:** Para las entradas `"10"`, `"5"` y `"+"`, la salida esperada es:

```
Resultado: 15.0
```

Para las entradas `"10"`, `"0"` y `"/"`, la salida esperada es:

```
Error: division por cero
```

Para las entradas `"10"`, `"5"` y `"x"`, la salida esperada es:

```
Operacion invalida
```

---

### Ejercicio 8 — `exercise_triangle.py`

**Archivo de test:** `test_tp3_triangle.py`

**Conceptos:** `input()`, `float()`, operadores lógicos (`and`), múltiples comparaciones.

**Consigna:** Leer tres números que representan los lados de un triángulo mediante `input()`. Verificar si pueden formar un triángulo válido e imprimir el resultado. Un triángulo es válido si la suma de dos lados cualesquiera es estrictamente mayor que el tercer lado (desigualdad triangular). Si la suma es igual, forman una línea recta, no un triángulo.

**Ejemplo:** Para las entradas `"3"`, `"4"` y `"5"`, la salida esperada es:

```
Los lados forman un triangulo valido
```

Para las entradas `"1"`, `"2"` y `"5"`, la salida esperada es:

```
Los lados no forman un triangulo valido
```

---

### Ejercicio 9 (Integrador) — `exercise_discount.py`

**Archivo de test:** `test_tp3_discount.py`

**Conceptos:** Todos los anteriores combinados: `input()`, `float()`, `int()`, `if-elif-else`, operadores de comparación, operaciones matemáticas, f-strings.

**Consigna:** Crear un sistema de descuentos para una tienda. Leer mediante `input()`:

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

**Ejemplo:** Para las entradas `"100"` y `"12"`, la salida esperada es:

```
Subtotal: 1200.0
Descuento aplicado: 20%
Monto de descuento: 240.0
Total final: 960.0
```

Para las entradas `"50"` y `"3"`, la salida esperada es:

```
Subtotal: 150.0
Descuento aplicado: 0%
Monto de descuento: 0.0
Total final: 150.0
```

---

### Ejercicio 10 — `exercise_password.py`

**Archivo de test:** `test_tp3_password.py`

**Conceptos:** `input()`, `len()`, operador `in`, múltiples ifs independientes, validación de strings.

**Consigna:** Leer una contraseña mediante `input()`. Validar que cumpla con los siguientes requisitos:
1. Debe tener al menos 8 caracteres de longitud
2. Debe contener al menos un número (usar el operador `in` para verificar cada dígito del 0 al 9)

Si cumple ambos requisitos, imprimir `"Contraseña valida"`. Si no cumple, imprimir cuál requisito falta (pueden ser uno o ambos).

**Ejemplo:** Para la entrada `"abc12345"`, la salida esperada es:

```
Contraseña valida
```

Para la entrada `"abc123"`, la salida esperada es:

```
Contraseña muy corta
```

Para la entrada `"abcdefgh"`, la salida esperada es:

```
Debe contener un numero
```

Para la entrada `"abc"`, la salida esperada es:

```
Contraseña muy corta
Debe contener un numero
```

---

### Ejercicio 11 (Desafío) — `exercise_leap_year.py`

**Archivo de test:** `test_tp3_leap_year.py`

**Conceptos:** `input()`, `int()`, operadores lógicos complejos (`and`, `or`), operador `%` (módulo), `if-else`.

**Consigna:** Leer un año mediante `input()`. Determinar si es un año bisiesto e imprimir el resultado. Un año es bisiesto si:
- Es divisible por 4, Y
- NO es divisible por 100, O es divisible por 400

**Ejemplo:** Para la entrada `"2000"`, la salida esperada es:

```
El año 2000 es bisiesto
```

Para la entrada `"2001"`, la salida esperada es:

```
El año 2001 no es bisiesto
```

Para la entrada `"1700"`, la salida esperada es:

```
El año 1700 no es bisiesto
```

---
