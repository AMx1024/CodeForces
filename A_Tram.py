n = int(input())
max, curr = 0, 0

for _ in range(n):
    exit, entry = map(int, input().split(" "))
    curr += entry - exit
    if curr > max:
        max = curr

print(max)
