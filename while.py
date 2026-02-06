contador = 1

while contador < 5:
    print(contador)
    contador += 1

#Ctrl + C (Cancel): Detiene lo que se esta ejecutando, el comando se ejecuta desde la terminal/consola


password = ""

while password != "miamorcito25":
    password = input("Ingresa la contraseña: ")

print("Acceso permitido")
    
suma = 0
numero = 1

while numero != 0:
    numero = int(input("Ingresa un numero (0 para salir): "))
    suma += numero #suma= suma + numero

print("LA suma total es: ", suma)