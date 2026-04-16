t = int(input())

for _ in range(t):
    skill1, skill2, skill12 = float("inf"), float("inf"), float("inf")
    n = int(input())
    found1, found2 = False, False
    for _ in range(n):
        t, skill = map(int, input().split(" "))
        if skill == 11 and t < skill12:
            skill12 = t
            found1, found2 = True, True
        else:
            if skill == 10 and t < skill1:
                skill1 = t
                found1 = True
            elif skill == 1 and t < skill2:
                skill2 = t
                found2 = True

    if found1 == True and found2 == True:
        print(skill12) if skill12 < skill1 + skill2 else print(skill1 + skill2)
    else:
        print(-1)

