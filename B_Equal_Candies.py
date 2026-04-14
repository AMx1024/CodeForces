t = int(input())

for _ in range(t):
    sum = 0
    n = int(input())
    arr = list(map(int, input().split()))
    minimum = min(arr)
    for num in arr:
        sum += (num - minimum)

    print(sum)

