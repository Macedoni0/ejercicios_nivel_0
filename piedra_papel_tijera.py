import random
def obtener_opcion_maquina():
opciones = ["piedra", "papel", "tijera"]
opcion = random.choice(opciones)
return opcion
def determinar_ganador(jugador, maquina):
if jugador == maquina:
return "Empate"
elif (
(jugador == "piedra" and maquina == "tijera") or
(jugador == "papel" and maquina == "piedra") or
(jugador == "tijera" and maquina == "papel")
):
return "Ganaste"
else:
return "La máquina ganó"
while True:
jugador = input("Elige una opcion (piedra, papel, tijera): ").lower()
if jugador not in ["piedra", "papel", "tijera"]:
print("Opcion invalida Elige otra vez")
continue
maquina = obtener_opcion_maquina()
print(f"La máquina eligio: {maquina}")
resultado = determinar_ganador(jugador, maquina)
print(f"Resultado: {resultado}")
jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
if jugar_nuevamente.lower() != "s":
break
