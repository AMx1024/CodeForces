n = int(input())

for _ in range(n):
    num = int(input())
    sum = 0
    while num > 0:
        x = num % 10
        num = num // 10
        sum += x
    print(sum)