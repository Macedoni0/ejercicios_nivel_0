abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abecedario_resultante = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]

print("Lista después de eliminar las letras en posiciones múltiplos de 3:")
print(abecedario_resultante)
