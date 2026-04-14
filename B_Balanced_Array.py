n = int(input())

for _ in range(n):
    m = int(input())

    if (m//2) % 2:
        print("NO")

    else:
        print("YES")
        arr_even = [2*i for i in range(1, m//2+1)]
        arr_odd = [2*i+1 for i in range(m//2-1)]
        x = sum(arr_even) - sum(arr_odd)
        arr_even.extend(arr_odd)
        arr_even.append(x)
        print(*arr_even)
    