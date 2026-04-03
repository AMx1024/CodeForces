n = input()
m = input()
res = []

for a, b in zip(n, m):
    a = int(a)
    b = int(b)
    res.append(str(a ^ b))

print("".join(res))