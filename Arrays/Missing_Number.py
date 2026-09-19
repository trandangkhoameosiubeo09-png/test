n = int(input())
a = list(map(int, input().split()))
 
total = 0
 
for i in range(1, n+1):
    total += i
 
cur_total = sum(a)
 
print(total - cur_total)