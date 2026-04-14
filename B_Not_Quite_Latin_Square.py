t = int(input())
mapping = {"A": 1, "B": 2, "C": 3}
mapping2 = {1: "A", 2: "B", 3: "C"}

for _ in range(3*t):
    arr = list(input())
    n = 6
    for ch in arr:
        if ch != "?":
            n -= mapping[ch]
            
    try:
        print(mapping2[n])
    except KeyError:
        continue

