# Biostats
# Small descriptive-statistics tool for biological measurements.
# Desktop Python version.
#
# Controls:
#   Enter on a blank line = calculate
#   C = calculate
#   B = previous value
#   F = next value
#   G = next group in two-sample mode
#   Q = return to menu
#
# Sample standard deviation is used (divide by n-1).
# At least 2 values are required before a result is shown.

def mean(values):
    """Arithmetic mean of a list of numbers."""
    return sum(values) / len(values)

def variance(values):
    """Sample variance (n-1)."""
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / (len(values) - 1)

def std_dev(values):
    """Sample standard deviation (n-1)."""
    return variance(values) ** 0.5

def show(values, label):
    """Print a compact numeric summary."""
    print("")
    print(label)
    print("n    =", len(values))
    print("min  =", min(values))
    print("max  =", max(values))
    print("mean =", mean(values))
    print("var  =", variance(values))
    print("sd   =", std_dev(values))

def pause():
    """Keep results on screen until Enter is pressed."""
    input("Continue: [Enter]")

def collect(data):
    """Collect numbers one at a time.

    Empty input calculates. B goes back, F goes forward,
    G ends the current group, Q returns to the menu.
    """
    if data is None:
        data = []
    pos = len(data)

    while True:
        msg = "Input value " + str(pos + 1)
        if pos < len(data):
            msg = msg + " [" + str(data[pos]) + "]"
        raw = input(msg + ": ").strip()
        cmd = raw.upper()

        if raw == "" or cmd == "C":
            return data
        if cmd == "Q":
            return None
        if cmd == "G":
            return data
        if cmd == "B":
            if pos > 0:
                pos = pos - 1
            continue
        if cmd == "F":
            if pos < len(data):
                pos = pos + 1
            continue

        try:
            value = float(raw.replace(",", "."))
        except ValueError:
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
    group_a = collect([])
    if group_a is None:
        return
    if len(group_a) < 2:
        print("Need 2+ in A")
        pause()
        return

    group_b = collect([])
    if group_b is None:
        return
    if len(group_b) < 2:
        print("Need 2+ in B")
        pause()
        return

    show(group_a, "A")
    show(group_b, "B")
    print("A-B =", mean(group_a) - mean(group_b))
    pause()

def help_menu():
    print("")
    print("-HELP MENU-")
    print("Enter calculate")
    print("C calculate")
    print("B go back")
    print("F forward")
    print("G next group")
    print("Q return to menu")
    pause()

def menu():
    while True:
        print("")
        print("-WELCOME TO BIOSTATS-")
        print("Select mode:")
        print("[1] One sample")
        print("[2] Two sample")
        print("[3] Help")
        print("[4] Exit")
        choice = input("Mode: ").strip()

        if choice == "1":
            one()
        elif choice == "2":
            two()
        elif choice == "3":
            help_menu()
        elif choice == "4" or choice.upper() == "Q":
            print("Goodbye!")
            break
        else:
            print("1-4")

if __name__ == "__main__":
    menu()