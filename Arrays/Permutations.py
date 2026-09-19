n = int(input())
 
res1 = []
res2 = []
 
 
if n >= 4:
    for i in range(1, n+1):
        if i % 2 == 0:
            res1.append(i)
 
        else:
            res2.append(i)
 
    res = res1 + res2
 
    for element in res:
        print(element, end = " ")
 
else:
    if n == 1:
        print(1)
    else:
        print("NO SOLUTION")