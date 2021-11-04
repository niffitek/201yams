import sys


def print_help():
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print("USAGE\n"
              "\t./201yams d1 d2 d3 d4 d5 c\n"
              "\nDESCRIPTION\n"
              "\td1\tvalue of the first die (0 if not thrown)\n"
              "\td2\tvalue of the second die (0 if not thrown)\n"
              "\td3\tvalue of the third die (0 if not thrown)\n"
              "\td4\tvalue of the fourth die (0 if not thrown)\n"
              "\td5\tvalue of the fifth die (0 if not thrown)\n"
              "\tc\texpected combination")
        sys.exit(0)
    elif len(sys.argv) != 7:
        sys.exit(84)


def check_dices():
    if len(sys.argv) == 7:
        for i in range(1, 6):
            try:
                value = int(sys.argv[i])
                if value > 6 or value < 0:
                    sys.exit(84)
            except ValueError:
                sys.exit(84)


def check_combination_len(combLen):
    comb = str(sys.argv[6])
    if len(comb) != combLen:
        sys.exit(84)
    try:
        if int(comb[combLen - 1]) < 1 or int(comb[combLen - 1]) > 6:
            sys.exit(84)
    except ValueError:
        sys.exit(84)


def check_combination_straight_len(combLen):
    comb = str(sys.argv[6])
    if len(comb) != combLen:
        sys.exit(84)
    try:
        if int(comb[combLen - 1]) < 5 or int(comb[combLen - 1]) > 6:
            sys.exit(84)
    except ValueError:
        sys.exit(84)


def check_combination():
    comb = str(sys.argv[6])
    if comb.startswith("pair_") or comb.startswith("four_") or comb.startswith("yams_"):
        check_combination_len(6)
    elif comb.startswith("three_"):
        check_combination_len(7)
    elif comb.startswith("straight_"):
        check_combination_straight_len(10)
    elif comb.startswith("full_"):
        if len(comb) != 8:
            sys.exit(84)
        try:
            if int(comb[5]) < 1 or int(comb[5]) > 6 or int(comb[7]) < 1 or int(comb[7]) > 6:
                sys.exit(84)
        except ValueError:
            sys.exit(84)
    else:
        sys.exit(84)


def check_input():
    print_help()
    check_dices()
    check_combination()
