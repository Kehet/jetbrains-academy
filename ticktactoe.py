prompt = input("Enter cells: ").replace("_", " ")

cells = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


def print_grid(cells):
    print("---------")

    for row in cells:
        print("| {} {} {} |".format(row[0], row[1], row[2]))

    print("---------")


def check_winner(cells):
    turns = {}
    turns.setdefault('X', 0)
    turns.setdefault('O', 0)
    turns.setdefault(' ', 0)

    for row in cells:
        turns[row[0]] += 1
        turns[row[1]] += 1
        turns[row[2]] += 1

    if abs(turns['X'] - turns['O']) > 1:
        return "Impossible"

    wins = {'X': 0, 'O': 0, ' ': 0}

    if cells[0][0] == cells[0][1] == cells[0][2]:
        wins[cells[0][0]] += 1
    if cells[1][0] == cells[1][1] == cells[1][2]:
        wins[cells[1][0]] += 1
    if cells[2][0] == cells[2][1] == cells[2][2]:
        wins[cells[2][0]] += 1
    if cells[0][0] == cells[1][0] == cells[2][0]:
        wins[cells[0][0]] += 1
    if cells[0][1] == cells[1][1] == cells[2][1]:
        wins[cells[0][1]] += 1
    if cells[0][2] == cells[1][2] == cells[2][2]:
        wins[cells[0][2]] += 1
    if cells[0][0] == cells[1][1] == cells[2][2]:
        wins[cells[0][0]] += 1
    if cells[0][2] == cells[1][1] == cells[2][0]:
        wins[cells[0][2]] += 1

    if (wins['X'] > 0 and wins['O'] > 0) or wins['X'] > 1 or wins['O'] > 1:
        return "Impossible"
    elif wins['X']:
        return 'X wins'
    elif wins['O']:
        return 'O wins'

    if (turns['X'] == 5 and turns['O'] == 4) or (turns['X'] == 4 and turns['O'] == 5):
        return "Draw"

    if turns['X'] == turns['O'] - 1 or turns['X'] == turns['O'] or turns['X'] - 1 == turns['O'] :
        return "Game not finished"

    return "Impossible"


def handle_turn():
    global turn
    while True:
        coords = input("Enter the coordinates: ").split()

        x = int(coords[0]) - 1
        y = int(coords[1]) - 1

        if x > 2 or x < 0 or y > 2 or y < 0:
            print("Coordinates should be from 1 to 3!")
            continue

        if cells[x][y] == " ":
            cells[x][y] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            break

        print("This cell is occupied! Choose another one!")


turn = 'X'

print_grid(cells)

while True:
    handle_turn()
    print_grid(cells)

    status = check_winner(cells)

    if status != "Game not finished":
        print(status)
        break
