k, n, w = map(int, input().split(" "))
price = int(k * w * (w+1) / 2)
print(max(price-n, 0))