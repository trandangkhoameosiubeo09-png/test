n = int(input())
 
res = []
 
res.append(n)
 
while n > 1:
    if n % 2 == 0:
        n = n // 2
        res.append(n)
 
    else:
        n = (n * 3) + 1
        res.append(n)
 
for element in res:
    print(element, end =" ")