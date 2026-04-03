n = int(input()) + 1

while True:
    str_n = str(n)
    s = set(map(int, str_n))
    if len(s) == len(str_n):
        print(str_n)
        break
    n += 1