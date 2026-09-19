n = int(input())
a = list(map(int, input().split()))
 
res = 0
 
for l in range(n-1):
    while a[l] > a[l+1]:
        add = a[l] - a[l+1]
        a[l+1] += add
        res += add
 
print(res)
 
