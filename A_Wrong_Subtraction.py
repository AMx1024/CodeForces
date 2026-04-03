n, k = map(int, input().split(" "))

while k > 0:
    x = n - (n // 10) * 10
    if n % 10:
        if x >= k:
            n -= k
            k = 0
            break
        
        else:
            n -= x
            k -= x
    else:
        n = n // 10
        k -= 1

print(n)