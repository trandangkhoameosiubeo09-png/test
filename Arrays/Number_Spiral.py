t = int(input())
 
for _ in range(t):
    y, x = map(int, input().split())
 
    k = max(y, x)
 
    if k % 2 == 0:
        if y == k:
            print(k * k - x + 1)
        else:
            print((k - 1) * (k - 1) + y)
    else:
        if x == k:
            print(k * k - y + 1)
        else:
            print((k - 1) * (k - 1) + x)
 