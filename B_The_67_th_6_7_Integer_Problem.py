t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    s = sum(arr) * -1
    m = max(arr)
    print(s+2*m)