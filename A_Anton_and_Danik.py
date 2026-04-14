a, d = 0, 0
n = int(input())
wins = input()
wins = list(map(str, wins))

for win in wins:
    if win == "A":
        a += 1
    else:
        d += 1

if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")