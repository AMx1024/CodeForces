t = int(input())

for _ in range(t):
    n = int(input())
    if n <= 2:
        print(0)
    else:
        if n % 2:
            print(n//2)
        else:
            print(n//2 - 1)
