
def HexToBin():
    n = input().strip()

    ans = []

    char = "0123456789ABCDEF"
    for i in n:
        value = char.index(i)

        bit = []
        for j in range(4):
            du = value % 2
            bit.append(du)  
            value //= 2

        bit.reverse()
        ans.append("".join(map(str, bit)))


    n = input().strip()

    r = len(n) % 4 
    if r != 0:
        n = "0" * (4-r) + n

    char = "0123456789ABCDEF"

    for i in range(0, len(n), 4):
        group = n[i:i + 4]

        value = 0

        for bit in group:
            value = value**2 + int(bit)

        ans += char[value]

    print(ans)
 
