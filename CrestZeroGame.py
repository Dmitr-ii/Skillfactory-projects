def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():
    print()
    print("    * 0 * 1 * 2 * ")
    print(" ", "*" * 15)
    for i, row in enumerate(field):
        row_str = f"  {i} * {' * '.join(row)} * "
        print(row_str)
        print(" ", "*" * 15)
    print()


def ask():
    while True:
        coords = input("         Ваш ход: ").split()

        if len(coords) != 2:
            print("  Введите 2 координаты! ")
            continue
        x, y = coords
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    for i in range(3):
        if field[i] == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if field[i] == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True

    for i in range(3):
        simbols = []
        for j in range(3):
            simbols.append(field[j][i])
        if simbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if simbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True

        simbols = []
        for i in range(3):
            simbols.append(field[i][i])
        if simbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if simbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True

        simbols = []
        for i in range(3):
            simbols.append(field[i][2 - i])
        if simbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if simbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True

    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break

