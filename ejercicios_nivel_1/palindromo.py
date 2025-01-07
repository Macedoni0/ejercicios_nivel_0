palabra = input("Introduce una palabra: ")
palabra = palabra.replace(" ", "").lower()
if palabra == palabra[::-1]:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")
