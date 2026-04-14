def perfect_square(n):
    root = n**0.5
    return True if abs(root - root//1) < 1e-10 else False

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    summation = sum(arr)
    print("YES") if perfect_square(summation) else print("NO")