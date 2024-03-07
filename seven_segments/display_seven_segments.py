def seven_segments_display(digits):
    segments = {
        0: ('a', 'b', 'c', 'd', 'e', 'f'),
        1: ('b', 'c'),
        2: ('a', 'b', 'd', 'e', 'g'),
        3: ('a', 'b', 'c', 'd', 'g'),
        4: ('b', 'c', 'f', 'g'),
        5: ('a', 'c', 'd', 'f', 'g'),
        6: ('a', 'c', 'd', 'e', 'f', 'g'),
        7: ('a', 'b', 'c'),
        8: ('a''b', 'c', 'd', 'e', 'f', 'g')
    }


for display in ("a", 'b', 'c', 'd', 'e', 'f', 'g'):
    if display in segments[digits]:
        print('1', end="")
    else:
        print('0', end="")

numbers = int(input("Enter a digit: "))

match numbers:
    case 0:
        print("* * *")
        print("*   *")
        print("*   *")
        print("* * *")

    case 1:
        print("    *")
        print("    *")
        print("    *")
        print("    *")

    case 2:
        print("***")
        print("   *")
        print("***")
        print("*   ")
        print("***")

    case 3:
        print("***")
        print("   *")
        print("***")
        print("   *")
        print("***")

    case 4:
        print("* *")
        print("* *")
        print("***")
        print("  *")
        print("  *")

    case 5:
        print("***")
        print("*  ")
        print("****")
        print("    *")
        print("***")

    case 6:
        print("****")
        print("*   ")
        print("* * *")
        print("*   *")
        print("* * *")

    case 7:
        print("****")
        print("   *")
        print("   *")
        print("   *")
        print("   *")

    case 8:
        print("* * *")
        print("*   * ")
        print("* * *")
        print("*   *")
        print("* * *")

    case 9:
        print("*****")
        print("*   *")
        print("*****")
        print("    *")
        print("    *")
