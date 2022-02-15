import random


def make_stock():
    pieces = []
    for i in range(0, 7):
        for j in range(0, 7):
            if not [min(i, j), max(i, j)] in pieces:
                pieces.append([min(i, j), max(i, j)])
    return pieces


def give_hand():
    global pieces

    hand = []
    for _ in range(7):
        index = random.randint(0, len(pieces["stock"]) - 1)
        hand.append(pieces["stock"][index])
        del pieces["stock"][index]

    return hand


def best_doubles(hand):
    best_value = None
    best_index = None

    for index, piece in enumerate(hand):
        if piece[0] == piece[1]:
            if best_value is None or piece[0] > best_value:
                best_value = piece[0]
                best_index = index

    return best_value, best_index


def set_starting(index, name):
    global current_player
    global pieces

    current_player = name
    pieces["snake"].append(pieces[name][index])
    del pieces[name][index]


def swap_current_player():
    global current_player

    if current_player == "player":
        current_player = "computer"
    else:
        current_player = "player"


def print_turn():
    print("=" * 70)
    print("Stock size:", len(pieces["stock"]))
    print("Computer pieces:", len(pieces["computer"]))
    print()

    if len(pieces["snake"]) < 6:
        for piece in pieces["snake"]:
            print(piece, end="")
        print()
    else:
        print(pieces["snake"][0], "...", end="", sep="")
        for piece in pieces["snake"][-3:]:
            print(piece, end="")
        print()

    print()
    print("Your pieces:")
    for (index, piece) in enumerate(pieces["player"]):
        print(index + 1, ":", piece, sep="")
    print()


def handle_command(command, current_player):
    global pieces

    if command > 0:
        command = command - 1

        if pieces[current_player][command][0] == pieces["snake"][-1][1]:
            pieces["snake"].append(pieces[current_player][command])
            del pieces[current_player][command]
        elif pieces[current_player][command][1] == pieces["snake"][-1][1]:
            pieces["snake"].append(pieces[current_player][command][::-1])
            del pieces[current_player][command]
        else:
            if current_player == "player":
                print("Illegal move. Please try again.")
            return False
    elif command < 0:
        command = abs(command) - 1

        if pieces[current_player][command][0] == pieces["snake"][0][0]:
            pieces["snake"].insert(0, pieces[current_player][command][::-1])
            del pieces[current_player][command]
        elif pieces[current_player][command][1] == pieces["snake"][0][0]:
            pieces["snake"].insert(0, pieces[current_player][command])
            del pieces[current_player][command]
        else:
            if current_player == "player":
                print("Illegal move. Please try again.")
            return False
    elif len(pieces["stock"]) > 0:
        index = random.randint(0, len(pieces["stock"]) - 1)
        pieces[current_player].append(pieces["stock"][index])
        del pieces["stock"][index]

    return True


def is_draw():
    global pieces

    if pieces['snake'][0][0] != pieces['snake'][-1][1]:
        return False

    count = 0
    for piece in pieces['snake']:
        if piece[0] == pieces['snake'][0][0]:
            count = count + 1

        if piece[1] == pieces['snake'][0][0]:
            count = count + 1

    return count > 7


def get_input_integer():
    global pieces
    global current_player

    while True:
        try:
            maybe_command = int(input())
        except ValueError:
            print("Invalid input. Please try again..")
            continue

        if maybe_command > len(pieces[current_player]) or maybe_command < -len(pieces[current_player]):
            print("Invalid input. Please try again..")
            continue

        return maybe_command


def calculate_score_for_moves():
    global pieces

    count = {i: 0 for i in range(7)}

    for piece in pieces['snake']:
        count[piece[0]] = count[piece[0]] + 1
        count[piece[1]] = count[piece[1]] + 1

    for piece in pieces['computer']:
        count[piece[0]] = count[piece[0]] + 1
        count[piece[1]] = count[piece[1]] + 1

    scores = {i: None for i in range(len(pieces['computer']))}

    for (index, piece) in enumerate(pieces['computer']):
        scores[index] = count[piece[0]] + count[piece[1]]

    return scores


current_player = None
pieces = {"stock": [], "computer": [], "player": [], "snake": []}
ai_scoreboard = None

while current_player is None:
    pieces["stock"] = make_stock()
    pieces["computer"] = give_hand()
    pieces["player"] = give_hand()

    value_computer, index_computer = best_doubles(pieces["computer"])
    value_player, index_player = best_doubles(pieces["player"])

    if value_player is not None and value_computer is None:
        set_starting(index_player, "player")
    elif value_player is None and value_computer is not None:
        set_starting(index_computer, "computer")
    elif value_player is not None and value_computer is not None:
        if value_player > value_computer:
            set_starting(index_player, "player")
        else:
            set_starting(index_computer, "computer")

while True:
    swap_current_player()
    print_turn()

    if len(pieces[current_player]) < 1:
        if current_player == "player":
            print("Status: The game is over. You won!")
        else:
            print("Status: The game is over. The computer won!")
        break

    if is_draw():
        print("Status: The game is over. It's a draw!")
        break

    if current_player == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
    else:
        print("Status: It's your turn to make a move. Enter your command.")

    while True:
        if current_player == "player":
            command = get_input_integer()
        else:
            if ai_scoreboard is None:
                ai_scoreboard = calculate_score_for_moves()

            if len(ai_scoreboard) > 0:
                command = max(ai_scoreboard, key=ai_scoreboard.get)
                del ai_scoreboard[command]
                command = command + 1
            else:
                command = 0

        if handle_command(command, current_player):
            ai_scoreboard = None
            break
