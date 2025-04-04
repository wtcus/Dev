while True:
    A = float(input("Введіть перше число:"))
    c = input("виберіть оператора: + - * / ")
    B = float(input("Введіть друге число:"))
    if c == "+":
        print(A + B)
    elif c == "-":
        print(A - B)
    elif c == "*":
        print(A * B)
    elif c == "/":
        if B != 0:
            print(A / B)
        else:
            print("ділення на нуль")
        break
    else:
        print("помилка")