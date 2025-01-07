#A
numero_secreto = 12
adivinanza = int(input("Adivina el número: "))
if adivinanza == numero_secreto:
    print("¡Acertaste!")
else:
    print("Numero fallido")

#B
numero_secreto = 8
adivinanza = int(input("Adivina el número: "))
while adivinanza != 8:
    if adivinanza == numero_secreto:
        print("¡Acertaste!")
    else:
        adivinanza = int(input("Adivina el número: "))

#C

numero_secreto = 15
adivinanza = int(input("Adivina el número: "))
for i in range(10):
    if adivinanza == numero_secreto:
        print("¡Acertaste!")
    else:
        adivinanza = int(input("Adivina el número: "))