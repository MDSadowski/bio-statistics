def mean(values):
    return sum(values) / len(values)

def sd(values):
    m = mean(values)
    v = 0
    for x in values:
        v = v + (x - m) ** 2
    v = v / (len(values) - 1)
    return v ** 0.5

def show(values, label):
    print("")
    print(label)
    print("n =", len(values))
    print("min =", min(values))
    print("max =", max(values))
    print("mean =", mean(values))
    print("sd =", sd(values))

def wait_bq():
    while True:
        raw = input("- back / quit: ")
        cmd = raw.strip()
        if cmd == "-" or cmd.upper() == "B":
            return "B"
        if cmd == "/" or cmd.upper() == "Q":
            return "Q"

def collect(title, data):
    if data is None:
        data = []
    pos = len(data)
    print("")
    print(title)
    print("EXE calc  - back")
    print("+ fwd  / menu  * grp")
    while True:
        msg = "V" + str(pos + 1)
        if pos < len(data):
            msg = msg + "=" + str(data[pos])
        try:
            raw = input(msg + ": ")
        except KeyboardInterrupt:
            return None
        raw = raw.strip()
        cmd = raw.upper()

        if raw == "":
            return data
        if raw == "/" or cmd == "Q":
            return None
        if raw == "*" or cmd == "G":
            return data
        if raw == "-" or cmd == "B":
            if pos > 0:
                pos = pos - 1
            continue
        if raw == "+" or cmd == "F":
            if pos < len(data):
                pos = pos + 1
            continue

        try:
            value = float(raw)
        except:
            print("num/EXE/-/+/ /")
            continue

        if pos < len(data):
            data[pos] = value
            data = data[:pos + 1]
        else:
            data.append(value)
        pos = len(data)

def one():
    data = []
    while True:
        data = collect("One sample", data)
        if data is None:
            return
        if len(data) < 2:
            print("Need 2+ values")
            return
        show(data, "sample")
        choice = wait_bq()
        if choice == "Q":
            return

def two():
    a = []
    b = []
    while True:
        print("A then *")
        a = collect("Group A", a)
        if a is None:
            return
        if len(a) < 2:
            print("Need 2+ in A")
            return
        b = collect("Group B", b)
        if b is None:
            return
        if len(b) < 2:
            print("Need 2+ in B")
            return
        show(a, "A")
        show(b, "B")
        print("A-B =", mean(a) - mean(b))
        choice = wait_bq()
        if choice == "Q":
            return

def help_menu():
    print("EXE calc")
    print("- back")
    print("+ fwd")
    print("* next grp")
    print("/ menu")
    input("/ quit: ")

while True:
    print("")
    print("Welcome to Biostats")
    print("Select mode:")
    print("1 One sample")
    print("2 Two sample")
    print("3 Help")
    print("4 Exit")
    try:
        choice = input("Mode: ")
    except KeyboardInterrupt:
        print("Bye")
        break
    choice = choice.strip()
    if choice == "1":
        one()
    elif choice == "2":
        two()
    elif choice == "3":
        help_menu()
    elif choice == "4" or choice == "/":
        print("Bye")
        break
    else:
        print("1-4")