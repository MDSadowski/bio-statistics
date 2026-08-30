def mean(values):
    return sum(values) / len(values)

def variance(values):
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / (len(values) - 1)

def std_dev(values):
    return variance(values) ** 0.5

def summarise(values, label):
    print("")
    print("Summary:", label)
    print("n    =", len(values))
    print("min  =", min(values))
    print("max  =", max(values))
    print("mean =", mean(values))
    print("var  =", variance(values))
    print("sd   =", std_dev(values))

def pause():
    input("Press Enter to continue...")

def collect_values(data=None):
    if data is None:
        data = []
    pos = len(data)

    while True:
        prompt = "Input value " + str(pos + 1)
        if pos < len(data):
            prompt = prompt + " [" + str(data[pos]) + "]"
        raw = input(prompt + ": ").strip()

        if raw == "":
            return data

        cmd = raw.upper()
        if cmd == "Q":
            return None
        if cmd == "C":
            return data
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

def one_sample():
    print("")
    print("ONE SAMPLE")
    data = collect_values()
    if data is None:
        return
    if len(data) < 2:
        print("Need at least 2 values.")
        pause()
        return
    summarise(data, "one sample")
    pause()

def two_sample():
    print("")
    print("TWO SAMPLE")
    group_a = collect_values()
    if group_a is None:
        return
    if len(group_a) < 2:
        print("Group A needs at least 2 values.")
        pause()
        return

    group_b = collect_values()
    if group_b is None:
        return
    if len(group_b) < 2:
        print("Group B needs at least 2 values.")
        pause()
        return

    summarise(group_a, "group A")
    summarise(group_b, "group B")
    print("")
    print("mean A - mean B =", mean(group_a) - mean(group_b))
    pause()

def show_help():
    print("")
    print("One-sample and two-sample controls")
    print("Enter = calculate")
    print("C     = calculate")
    print("B     = back one value")
    print("F     = forward one value")
    print("G     = next group in two-sample mode")
    print("Q     = return to menu")
    pause()

def menu():
    while True:
        print("")
        print("Welcome to Biostats")
        print("Select mode:")
        print("1  One-sample stats")
        print("2  Two-sample comparison")
        print("3  Help")
        print("4  Exit")
        choice = input("Mode: ").strip()

        if choice == "1":
            one_sample()
        elif choice == "2":
            two_sample()
        elif choice == "3":
            show_help()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2, 3 or 4.")

if __name__ == "__main__":
    menu()