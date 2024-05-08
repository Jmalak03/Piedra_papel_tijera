import random


def obtener_movimiento_usuario():
    while True:
        movimiento = input(
            "Elige piedra, papel o tijera (o 'salir' para terminar): ").lower(
            )
        if movimiento in ['piedra', 'papel', 'tijera', 'salir']:
            return movimiento
        else:
            print(
                "Movimiento inválido. Por favor, elige piedra, papel, tijera o 'salir'."
            )


def obtener_movimiento_cpu():
    return random.choice(['piedra', 'papel', 'tijera'])


def determinar_ganador(usuario, cpu):
    if usuario == cpu:
        return "Empate"
    elif (usuario == 'piedra' and cpu == 'tijera') or \
         (usuario == 'papel' and cpu == 'piedra') or \
         (usuario == 'tijera' and cpu == 'papel'):
        return "¡Ganaste!"
    else:
        return "¡La CPU gana!"


def jugar():
    print("Bienvenido al juego de Piedra, Papel o Tijera")
    while True:
        usuario = obtener_movimiento_usuario()
        if usuario == 'salir':
            print("¡Gracias por jugar!")
            break
        cpu = obtener_movimiento_cpu()
        print("La CPU elige:", cpu)
        resultado = determinar_ganador(usuario, cpu)
        print(resultado)


if __name__ == "__main__":
    jugar()
