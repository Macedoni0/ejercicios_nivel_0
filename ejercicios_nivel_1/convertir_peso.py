def convertir_peso():
    try:
        peso = float(input("Introduce tu peso: "))
        unidad = input("(K)g o (L)bs? ").strip().upper()
        if unidad == "K":
            peso_en_libras = peso / 0.45
            print(f"Tu peso en libras es: {peso_en_libras:.2f} lbs")
        elif unidad == "L":
            peso_en_kilos = peso * 0.45
            print(f"Tu peso en kilogramos es: {peso_en_kilos:.2f} kg")
        else:
            print("Unidad no reconocida, por favor introduce 'K' para kilogramos o 'L' para libras")
    except ValueError:
        print("Por favor introduce un numero valido")
convertir_peso()