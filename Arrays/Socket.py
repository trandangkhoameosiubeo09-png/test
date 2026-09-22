n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)
socket = 0
res = 0
if m == 1:
    print("0")

else:
    for i in range(len(a)):
        socket += a[i]
        res += 1
        if socket >= m:
            print(res)
            break
        
        socket -= 1
    if socket < m:
        print(-1)
