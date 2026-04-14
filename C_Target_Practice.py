n = int(input())

for _ in range(n):
    sum = 0
    for i in range(10):
        arr = list(input())
        for j in range(10):
            if arr[j] == "X":
                idx_1 = i if i < 5 else 9-i
                idx_2 = j if j < 5 else 9-j
                idx = min(idx_1, idx_2)

                sum += (idx+1)
    print(sum)