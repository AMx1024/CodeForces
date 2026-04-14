t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    prod = 1
    minimum, maximum = float("inf"), float("-inf")

    # Handling zero
    zero = 0
    for num in arr:
        if num == 0:
            zero += 1
        else:
            prod *= num
            minimum = min(minimum, num)
            maximum = max(maximum, num)
        

    if zero > 1:
        print(0)
    elif zero == 1:
        print(prod)
    else:
        prod = max(prod + prod//minimum, prod + prod//maximum)
        print(prod)

