# Biostats
# Small descriptive-statistics tool for biological measurements.
# Casio fx-CG50 MicroPython version.
#
# Casio controls (no ALPHA key needed):
#   EXE on a blank line = calculate
#   - = previous value
#   + = next value
#   * = next group in two-sample mode
#   / = return to menu
#
# Sample standard deviation is used (divide by n-1).
# At least 2 values are required before a result is shown.
# Use the filename biostats.py (no hyphen) on the calculator.

def mean(values):
    """Arithmetic mean of a list of numbers."""
    return sum(values) / len(values)

def sd(values):
    """Sample standard deviation (n-1)."""
    m = mean(values)
    v = 0
    for x in values:
        v = v + (x - m) ** 2
    v = v / (len(values) - 1)
    return v ** 0.5

def show(values, label):
    """Print a compact summary for the calculator screen."""
    print("")
    print(label)
    print("n =", len(values))
    print("min =", min(values))
    print("max =", max(values))
    print("mean =", mean(values))
    print("sd =", sd(values))

def pause():
    """Keep results on screen until EXE is pressed."""
    input("Continue: [EXE]")

def collect(data):
    """Collect numbers one at a time.

    Empty input calculates. '-' goes back, '+' goes forward,
    '*' ends the current group, '/' returns to the menu.
    """
    if data is None:
        data = []
    pos = len(data)
    while True:
        msg = "Input value " + str(pos + 1)
        if pos < len(data):
            msg = msg + " [" + str(data[pos]) + "]"
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
            continue

        if pos < len(data):
            data[pos] = value
            data = data[:pos + 1]
        else:
            data.append(value)
        pos = len(data)

def one():
    print("")
    print("-ONE SAMPLE MODE-")
    data = collect([])
    if data is None:
        return
    if len(data) < 2:
        print("Need 2+ values")
        pause()
        return
    show(data, "sample")
    pause()

def two():
    print("")
    print("-TWO SAMPLE MODE-")
    a = collect([])
    if a is None:
        return
    if len(a) < 2:
        print("Need 2+ in A")
        pause()
        return
    b = collect([])
    if b is None:
        return
    if len(b) < 2:
        print("Need 2+ in B")
        pause()
        return
    show(a, "A")
    show(b, "B")
    print("A-B =", mean(a) - mean(b))
    pause()

def help_menu():
    print("")
    print("-HELP MENU-")
    print("EXE calculate")
    print("- go back")
    print("+ forward")
    print("* next group")
    print("/ return to menu")
    pause()

while True:
    print("")
    print("-WELCOME TO BIOSTATS-")
    print("Select mode:")
    print("[1] One sample")
    print("[2] Two sample")
    print("[3] Help")
    print("[4] Exit")
    try:
        choice = input("Mode: ")
    except KeyboardInterrupt:
        print("Goodbye!")
        break
    choice = choice.strip()
    if choice == "1":
        one()
    elif choice == "2":
        two()
    elif choice == "3":
        help_menu()
    elif choice == "4" or choice == "/":
        print("Goodbye!")
        break
    else:
        print("1-4")