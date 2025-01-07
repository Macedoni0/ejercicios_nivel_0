palabra = input("Introduce una palabra: ")
palabra = palabra.lower()
vocales = "aeiou"
conteo_vocales = {vocal: 0 for vocal in vocales}

for letra in palabra:
    if letra in vocales:
        conteo_vocales[letra] += 1

print("Numero de veces que aparece cada vocal:")
for vocal, cantidad in conteo_vocales.items():
    print(f"{vocal.upper()}: {cantidad}")
