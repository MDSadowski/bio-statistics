# Biostats Plus
# Clinical extras for small
# biological datasets.
# Casio fx-CG50 MicroPython.
# Printed lines <= 21 chars.
#
# EXE blank = calculate
# - back   + forward
# * next group
# / menu
# Menu pages:
# P1 page 1   P2 page 2
# + next page - prev page

def mean(values):
    return sum(values) / len(values)

def variance(values):
    m = mean(values)
    v = 0
    for x in values:
        v = v + (x - m) ** 2
    return v / (len(values) - 1)

def sd(values):
    return variance(values) ** 0.5

def median(values):
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return 0.5 * (s[mid - 1] + s[mid])

def iqr(values):
    s = sorted(values)
    n = len(s)
    if n % 2 == 0:
        q1 = median(s[:n // 2])
        q3 = median(s[n // 2:])
    else:
        q1 = median(s[:n // 2])
        q3 = median(s[n // 2 + 1:])
    return q3 - q1

def r4(x):
    return round(x, 4)

def pause():
    input("Continue: [EXE]")

def page_mark(page, total):
    tag = "[" + str(page) + "/" + str(total) + "]"
    return " " * (21 - len(tag)) + tag

def show_menu(page):
    print("")
    print("-BIOSTATS PLUS-")
    print("Select mode:")
    if page == 1:
        print("[1] Descriptive")
        print("[2] Group compare")
        print("[3] Paired diff")
        print("[4] Proportion")
        print("+ next page")
    else:
        print("[5] 2x2 test")
        print("[6] Cutoff")
        print("[7] Help")
        print("[8] Exit")
        print("- prev page")
    print(page_mark(page, 2))

def collect(data, label):
    if data is None:
        data = []
    pos = len(data)
    while True:
        msg = label + " " + str(pos + 1)
        if pos < len(data):
            msg = msg + "[" + str(data[pos]) + "]"
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

def show_desc(values, title):
    print(title)
    print("n =", len(values))
    print("min =", r4(min(values)))
    print("max =", r4(max(values)))
    print("mean =", r4(mean(values)))
    print("sd =", r4(sd(values)))
    print("med =", r4(median(values)))
    print("IQR =", r4(iqr(values)))

def ask_num(prompt):
    while True:
        try:
            raw = input(prompt)
        except KeyboardInterrupt:
            return None
        raw = raw.strip()
        if raw == "/" or raw.upper() == "Q":
            return None
        try:
            return float(raw)
        except:
            continue

def descriptive():
    print("")
    print("-DESCRIPTIVE-")
    data = collect([], "Input value")
    if data is None:
        return
    if len(data) < 2:
        print("Need 2+ values")
        pause()
        return
    show_desc(data, "sample")
    pause()

def group_compare():
    print("")
    print("-GROUP COMPARE-")
    a = collect([], "A value")
    if a is None:
        return
    if len(a) < 2:
        print("Need 2+ in A")
        pause()
        return
    b = collect([], "B value")
    if b is None:
        return
    if len(b) < 2:
        print("Need 2+ in B")
        pause()
        return
    show_desc(a, "A")
    show_desc(b, "B")
    diff = mean(a) - mean(b)
    n1 = len(a)
    n2 = len(b)
    sp2 = ((n1 - 1) * variance(a) + (n2 - 1) * variance(b))
    sp2 = sp2 / (n1 + n2 - 2)
    se = (sp2 * (1.0 / n1 + 1.0 / n2)) ** 0.5
    t = diff / se
    d = diff / (sp2 ** 0.5)
    print("A-B =", r4(diff))
    print("t =", r4(t))
    print("df =", n1 + n2 - 2)
    print("d =", r4(d))
    pause()

def paired_diff():
    print("")
    print("-PAIRED DIFF-")
    data = collect([], "Input diff")
    if data is None:
        return
    if len(data) < 2:
        print("Need 2+ diffs")
        pause()
        return
    show_desc(data, "diffs")
    se = sd(data) / (len(data) ** 0.5)
    t = mean(data) / se
    print("t =", r4(t))
    print("df =", len(data) - 1)
    pause()

def proportion():
    print("")
    print("-PROPORTION-")
    k = ask_num("Successes: ")
    if k is None:
        return
    n = ask_num("Trials: ")
    if n is None:
        return
    if n <= 0 or k < 0 or k > n:
        print("Need 0<=k<=n")
        pause()
        return
    p = k / n
    se = (p * (1.0 - p) / n) ** 0.5
    lo = p - 1.96 * se
    hi = p + 1.96 * se
    if lo < 0:
        lo = 0
    if hi > 1:
        hi = 1
    print("p =", r4(p))
    print("CI lo =", r4(lo))
    print("CI hi =", r4(hi))
    pause()

def two_by_two():
    print("")
    print("-2x2 TEST-")
    tp = ask_num("True pos: ")
    if tp is None:
        return
    fp = ask_num("False pos: ")
    if fp is None:
        return
    fn = ask_num("False neg: ")
    if fn is None:
        return
    tn = ask_num("True neg: ")
    if tn is None:
        return
    if min(tp, fp, fn, tn) < 0:
        print("Need counts >= 0")
        pause()
        return
    if (tp + fn) > 0:
        sens = tp / (tp + fn)
    else:
        sens = 0
    if (tn + fp) > 0:
        spec = tn / (tn + fp)
    else:
        spec = 0
    if (tp + fp) > 0:
        ppv = tp / (tp + fp)
    else:
        ppv = 0
    if (tn + fn) > 0:
        npv = tn / (tn + fn)
    else:
        npv = 0
    print("sens =", r4(sens))
    print("spec =", r4(spec))
    print("PPV =", r4(ppv))
    print("NPV =", r4(npv))
    pause()

def cutoff():
    print("")
    print("-CUTOFF CHECK-")
    data = collect([], "Input value")
    if data is None:
        return
    if len(data) < 1:
        print("Need 1+ values")
        pause()
        return
    cut = ask_num("Cutoff: ")
    if cut is None:
        return
    above = 0
    for x in data:
        if x >= cut:
            above = above + 1
    print("n =", len(data))
    print("cutoff =", r4(cut))
    print("above =", above)
    print("%above =", r4(100.0 * above / len(data)))
    pause()

def help_menu():
    print("")
    print("-HELP MENU-")
    print("EXE calculate")
    print("- go back")
    print("+ forward")
    print("* next group")
    print("/ return menu")
    print("P1 page 1")
    print("P2 page 2")
    pause()

page = 1
while True:
    show_menu(page)
    try:
        choice = input("Mode: ")
    except KeyboardInterrupt:
        print("Goodbye!")
        break
    choice = choice.strip().upper()
    if choice == "P1":
        page = 1
        continue
    if choice == "P2":
        page = 2
        continue
    if choice == "+" or choice == "N":
        page = 2
        continue
    if choice == "-":
        page = 1
        continue
    if choice == "1":
        descriptive()
    elif choice == "2":
        group_compare()
    elif choice == "3":
        paired_diff()
    elif choice == "4":
        proportion()
    elif choice == "5":
        two_by_two()
    elif choice == "6":
        cutoff()
    elif choice == "7":
        help_menu()
    elif choice == "8" or choice == "/":
        print("Goodbye!")
        break
    else:
        print("1-8 or P1/P2")