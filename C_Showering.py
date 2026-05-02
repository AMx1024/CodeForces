t = int(input())

for _ in range(t):
    n, s, m = map(int, input().split())
    task = []
    for _ in range(n):
        l, r = map(int, input().split())
        task.append([l, r])
    
    
    t_max = task[0][0]

    for i in range(n-1):
        t_curr = task[i+1][0] - task[i][1]
        t_max = max(t_curr, t_max)

    t_max = max(t_max, (m - task[-1][1]))


    if s <= t_max:
        print("YES")
    else:
        print("NO")