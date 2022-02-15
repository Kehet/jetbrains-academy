# write your code here

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

someMessages = {
    10: "Are you sure? It is only one digit! (y / n)",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
    12: "Last chance! Do you really want to embarrass yourself? (y / n)",
}

memory = 0


def is_one_digit(v):
    return -10 < v < 10 and v == int(v)


def check(_x, _y, _oper):
    msg = ""

    if is_one_digit(_x) and is_one_digit(_y):
        msg = msg + msg_6

    if (_x == 1.0 or _y == 1.0) and _oper == "*":
        msg = msg + msg_7

    if (_x == 0.0 or _y == 0.0) and (_oper == "*" or _oper == "+" or _oper == "-"):
        msg = msg + msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)

    calc = input()
    x, oper, y = calc.split()

    if x == "M":
        x = memory

    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if oper != "+" and oper != "-" and oper != "*" and oper != "/":
        print(msg_2)
        continue

    check(x, y, oper)

    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y != 0:
        result = x / y
    else:
        print(msg_3)
        continue

    print(result)

    while True:
        print(msg_4)
        store = input()

        if store == "y":

            if not is_one_digit(result):
                memory = result
                break

            msg_index = 10

            while msg_index <= 12:
                print(someMessages[msg_index])
                answer = input()

                if answer == "y":
                    if msg_index < 12:
                        msg_index = msg_index + 1
                    else:
                        memory = result
                        break
                elif answer == "n":
                    break

            break
        elif store == "n":
            break

    keepLooping = False
    while True:
        print(msg_5)
        doContinue = input()

        if doContinue == "y":
            keepLooping = True
            break
        elif doContinue == "n":
            break

    if not keepLooping:
        break
