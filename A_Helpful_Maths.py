s = input("")
s = [char for char in s if char != "+"]
n = len(s)

low, mid, high = 0, 0, n-1

while mid <= high:
    if s[mid] == "1":
        s[low], s[mid] = s[mid], s[low]
        low += 1
        mid += 1
    elif s[mid] == "2":
        mid += 1
    elif s[mid] == "3":
        s[mid], s[high] = s[high], s[mid]
        high -= 1
        

print("+".join(s))