n = int(input())
sum1 = 0
a1 = []
a2 = []

total = n*(n+1) / 2
if total % 2 == 0:
    target = total // 2

    for i in range(n, 0, -1):
        if sum1 < target and sum1 + i <= target:
            a1.append(i)
            sum1 += i

        else:
            a2.append(i)

    print("YES")
    print(len(a1))
    print(" ".join(map(str, a1)))
    print(len(a2))
    print(" ".join(map(str, a2)))

else:
    print("NO")



        
