import random
num_secreto = random.randint(1, 100)
intentos = 0
adivinado = False
print("Adivina el numero entre 1 y 100")
while not adivinado:
try:
guess = int(input("Ingresa un numero: "))
intentos += 1
if guess == num_secreto:
adivinado = True
elif guess < num_secreto:
print("El numero es mayor. Intenta de nuevo")
else:
print("El numero es menor. Intenta de nuevo")
except ValueError:
print("Por favor, ingresa un numero valido")
print(f"Adivinaste el numero:{num_secreto} en {intentos} intentos")