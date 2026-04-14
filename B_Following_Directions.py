t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(input())
    i, j = 0, 0
    passed = False

    for order in arr:
        if order == "U":
            j += 1
        elif order == "D":
            j -= 1
        elif order == "L":
            i -= 1
        elif order == "R":
            i += 1

        if i == 1 and j == 1:
            passed = True

    print("YES") if passed else print("NO")

