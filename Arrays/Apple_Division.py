n = int(input())
apples = list(map(int, input().split()))
 
total = sum(apples)
res = 10**18
def dfs(i, cur_sum):
    global res
 
    dif = abs(cur_sum - (total - cur_sum))
 
    if i >= len(apples):
        res = min(res, dif)
        return
 
    dfs(i+1, (cur_sum + apples[i]))
    dfs(i+1, cur_sum)
 
 
dfs(0, 0)
 
print(res)