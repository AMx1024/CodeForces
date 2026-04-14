t = int(input())

for _ in range(t):
    curr, maximum = 0,0
    n = int(input())
    arr = list(map(int, input().split()))
    
    for num in arr:
        if num == 0:
            curr += 1
            maximum = max(curr, maximum)

        else:
            curr = 0

    print(maximum)