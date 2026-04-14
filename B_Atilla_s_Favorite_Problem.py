t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(input())
    arr = [ord(str) for str in arr]
    maximum = max(arr)
    print(maximum - 96)
