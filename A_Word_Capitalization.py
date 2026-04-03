s = input()
s = s[0].upper() + s[1:] if len(s) > 1 else s[0].upper()
print(s)