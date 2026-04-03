n = int(input())
solved  = 0

for _ in range(n):
    soln = input().split()
    views = 0
    for view in soln:
        if view == "1":
            views += 1
    if views >= 2:
        solved += 1

print(solved)