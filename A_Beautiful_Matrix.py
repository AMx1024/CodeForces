idx = 0

for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        if arr[j] == 1:
            idx = [i, j]

print(abs(idx[0] - 2) + abs(idx[1] - 2))