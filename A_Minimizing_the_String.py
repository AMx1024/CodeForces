n = int(input())
string = input()

if n <= 1:
    print("")
    
    
else:
    done = False
    for i in range(n-1):
        if string[i] > string[i+1]:
            idx = i
            done = True
            break

    print(string[:idx] + string[idx+1:]) if done else print(string[:n-1])


