t = int(input())

for _ in range(t):
    n = list(input())
    i = len(n) - 1
    for j in range(len(n)):
        n[j] = int(n[j]) * (10**i)
        i -= 1
    i = 0
    for num in n:
        if num != 0:
            i += 1
    
    print(i)
    
    for num in n:
        if num != 0:
            print(num, end = " ")
        
    print()
    