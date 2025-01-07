numeros = []
for i in range(6):  
    while True:
        try:
            numero = int(input(f"Introduce el número ganador {i+1}: "))
            if 1 <= numero <= 49: 
                numeros.append(numero)
                break
            else:
                print("Por favor, introduce un numero entre 1 y 49")
        except ValueError:
            print("Por favor, introduce un numero valido")

numeros.sort()
print("Los numeros ganadores de la loteria primitiva, ordenados de menor a mayor son:")
print(numeros)
