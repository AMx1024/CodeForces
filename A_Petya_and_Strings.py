s1 = input().lower()
s2 = input().lower()
done = False
for i in range(len(s1)):
    if s1[i] > s2[i]:
        print(1)
        done = True
        break
    elif s1[i] < s2[i]:
        print(-1)
        done = True
        break
if done == False:
    print(0) 