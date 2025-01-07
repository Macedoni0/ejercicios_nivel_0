asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
asignaturas_a_repetir = []
for asignatura in asignaturas:
    while True:
        try:
            nota = float(input(f"Introduce la nota obtenida en {asignatura}: "))
            if 0 <= nota <= 10:  
                if nota >= 5: 
                    print(f"{asignatura} aprobada")
                else:  
                    asignaturas_a_repetir.append(asignatura)
                break
            else:
                print("Por favor, introduce una nota valida entre 0 y 10")
        except ValueError:
            print("Por favor, introduce una nota valida")

print("Asignaturas que debes repetir:")
print(asignaturas_a_repetir)
