s = input()
u, l = 0, 0

for char in s:
    if char.isupper():
        u += 1
    else:
        l += 1

print(s.lower()) if l >= u else print(s.upper())