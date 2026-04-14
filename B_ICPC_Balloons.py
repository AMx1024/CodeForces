from collections import Counter

n = int(input())

for _ in range(n):
    m = int(input())
    s = input()
    s_dict = Counter(s)
    sum = 0
    for key, value in s_dict.items():
        if value == 1:
            sum += 2
        else:
            sum += (value+1)
    print(sum)        