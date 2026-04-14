t = int(input())
mapping = {"p": "q", "q": "p", "w": "w"}

for _ in range(t):
    string = input()
    n = len(string)
    for i in range(n-1, -1, -1):
        print(mapping[string[i]], end="")

    print()