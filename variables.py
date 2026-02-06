nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)

nombre = "Sara"      # str
nombre = 2
edad = 27            # int
altura = 1.70        # float
activo = True        # bool

"""
Python es un lenguaje de programación fuerte y dinamicamente tipado (respeta las vrbles)

operadores_python.py
Ejemplos de operadores en Python (todo en un solo archivo).
"""

print("=" * 60)
print("1) OPERADORES ARITMÉTICOS")
print("=" * 60)

a = 10
b = 3
print("a =", a, "| b =", b)
print("a + b  =", a + b)    # suma
print("a - b  =", a - b)    # resta
print("a * b  =", a * b)    # multiplicación
print("a / b  =", a / b)    # división (float)
print("a // b =", a // b)   # división entera
print("a % b  =", a % b)    # residuo (módulo)
print("a ** b =", a ** b)   # potencia

print("\n" + "=" * 60)
print("2) OPERADORES DE ASIGNACIÓN")
print("=" * 60)

x = 5
print("x inicial =", x)

x += 2 # x = x + 2
print("x += 2 ->", x)

x -= 1 # x = x - 1
print("x -= 1 ->", x)

x *= 3 # x = x * 3
print("x *= 3 ->", x)

x /= 2 # x = x / 2
print("x /= 2 ->", x)

x //= 2
print("x //= 2 ->", x)

x %= 3
print("x %= 3 ->", x)

x **= 2
print("x **= 2 ->", x)

print("\n" + "=" * 60) #\n es un salto de linea
print("3) OPERADORES DE COMPARACIÓN") #Solo dan respuesta de True or False
print("=" * 60)

a = 10
b = 3
print("a =", a, "| b =", b)
print("a == b ->", a == b)  # igual
print("a != b ->", a != b)  # diferente
print("a > b  ->", a > b)   # mayor
print("a < b  ->", a < b)   # menor
print("a >= b ->", a >= b)  # mayor o igual
print("a <= b ->", a <= b)  # menor o igual

print("\n" + "=" * 60)
print("4) OPERADORES LÓGICOS")
print("=" * 60)

edad = 20
tiene_dni = True
print("edad =", edad, "| tiene_dni =", tiene_dni)
print("(edad >= 18) and tiene_dni ->", (edad >= 18) and tiene_dni)
print("(edad >= 18) or False      ->", (edad >= 18) or False)
print("not tiene_dni              ->", not tiene_dni)

print("\n" + "=" * 60)
print("5) OPERADORES DE PERTENENCIA (in / not in)")
print("=" * 60)

lista = ["harina", "aceite", "agua"] #Arreglos pueden tener str, int, bools, floats; la lista empieza desde el indice 0, el tamaño sin embargo es 3.
print("lista =", lista)
print("'aceite' in lista     ->", "aceite" in lista)
print("'torta' not in lista  ->", "torta" not in lista)

print("\n" + "=" * 60)
print("6) OPERADORES DE IDENTIDAD (is / is not)")
print("=" * 60)

a = [1, 2] #Estoy instanciando a la clase list, entonces la var "a" es un objeto
print(a.count) #count es el método del objeto "a"
b = [1, 2]
c = a
print("a =", a, "| b =", b, "| c = a")
print("a == b ->", a == b, " (mismo contenido)")
print("a is b ->", a is b, " (mismo objeto en memoria?)")
print("a is c ->", a is c, " (c apunta al mismo objeto que a)")
print("a is not b ->", a is not b)

print("\n" + "=" * 60)
print("7) OPERADORES BIT A BIT (bitwise)")
print("=" * 60)

a = 6   # 110 en binario  ... (1) 2^2  + (1) 2^1  + (0) 2^0 = 6
b = 3   # 011 en binario  ... (0) 2^2  + (1) 2^1  + (1) 2^0 = 3
print("a =", a, "(bin:", bin(a), ")")
print("b =", b, "(bin:", bin(b), ")")
print("a & b  ->", a & b,  "(AND)  bin:", bin(a & b))
print("a | b  ->", a | b,  "(OR)   bin:", bin(a | b))
print("a ^ b  ->", a ^ b,  "(XOR)  bin:", bin(a ^ b))
print("~a     ->", ~a,     "(NOT)  bin:", bin(~a))
print("a << 1 ->", a << 1, "(shift izq) bin:", bin(a << 1))
print("a >> 1 ->", a >> 1, "(shift der) bin:", bin(a >> 1))

print("\n" + "=" * 60)
print("8) OPERADOR WALRUS (:=)")
print("=" * 60)

texto = "hola"
if (n := len(texto)) > 3: #:= es una variable de asignacion de valor
    print("texto =", texto, "| len =", n, "-> Es mayor que 3")

print("\n" + "=" * 60)
print("FIN")
print("=" * 60)
