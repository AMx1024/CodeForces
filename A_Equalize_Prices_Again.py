from math import ceil
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    summation = sum(arr)
    print(ceil(summation // n))