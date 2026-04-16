t = int(input())

for _ in range(t):
    n = int(input())
    water = list(map(int, input().split()))

    total = sum(water)
    if total % n != 0:
        print("NO")
        continue

    avg = total // n

    prefix = 0
    possible = True

    for i in range(n):
        prefix += water[i]
        if prefix < (i + 1) * avg:
            print("NO")
            possible = False
            break

    if possible:
        print("YES")