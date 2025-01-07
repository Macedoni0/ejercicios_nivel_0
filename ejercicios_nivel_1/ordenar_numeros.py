def ordena_positivos(lista):
    positivos_ordenados = sorted([num for num in lista if num > 0])
    resultado = []
    indice_positivos = 0

    for num in lista:
        if num > 0:
            resultado.append(positivos_ordenados[indice_positivos])
            indice_positivos += 1
        else:
            resultado.append(num)

    return resultado

lista_ejemplo = [3, -1, 2, -7, 5, -3]
resultado = ordena_positivos(lista_ejemplo)
print("Lista original:", lista_ejemplo)
print("Lista con positivos ordenados:", resultado)
