n, m, diff = map(int, input().split())
applicant = list(map(int, input().split()))
apartment = list(map(int, input().split()))


queries = []
for x in applicant:
    queries.append([x-diff,x+diff])

queries.sort()
apartment.sort()
count = 0
i = 0
j = 0

while i < len(queries) and j < len(apartment):
    l, r = queries[i]

    if apartment[j] < l:
        j += 1

    elif apartment[j] > r:
        i += 1

    else:
        i += 1
        j +=1
        count +=1
 
print(count)

