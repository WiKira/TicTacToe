from table import Table
from player import Player

_table = Table()

name = input("Qual seu nome  player 1?")
simbol = input("Jogar com X ou O?").upper()

while simbol != "X" and simbol != "O":
    simbol = input("\nValor inválido, informe novamente.\nJogar com X ou O?").upper()

if simbol == "X":
    simbol = 1
else:
    simbol = -1

p1 = Player(name, simbol)

name = input("\nQual seu nome player 2?")

if simbol == 1:
    simbol = -1
else:
    simbol = 1

p2 = Player(name, simbol)

jogo_continua = True
player_turno = p1

print("\n" * 100)

_table.print_table()

while jogo_continua:
    print(f"Turno de {player_turno.name}:")
    position = input("Entre com a linha e coluna que deseja marcar (Formato: '3, 4'):")

    try:
        position = position.split(',')
        x, y = int(position[0].strip()), int(position[1].strip())
    except ValueError:
        print("Posição inválida. Tente novamente.\n")
        continue

    positionUpdated, texto = _table.update_position(x, y, player_turno.simbol)

    if not positionUpdated:
        print(texto)
        continue

    jogo_continua = not _table.verify_winner(x, y)

    if jogo_continua and 0 not in _table.table.values():
        jogo_continua = False
        print("\nVELHA")
    elif not jogo_continua:
        print(f"\nJogador {player_turno.name} é o vencedor")
        jogo_continua = False
    else:
        if player_turno == p1:
            player_turno = p2
        else:
            player_turno = p1

    print("\n" * 100)
    _table.print_table()
