def MAP(): return list(map(int,input().split()))

n,A,B,C = MAP()
l = [int(input()) for _ in range(n)]
INF = 10**9

def dfs(cur,a,b,c):
    if cur == n:
        return abs(a-A) + abs(b-B) + abs(c-C) -30 if min(a,b,c)>0 else INF
    ret0 = dfs(cur+1,a,b,c)
    ret1 = dfs(cur+1,a+l[cur],b,c)+10
    ret2 = dfs(cur+1,a,b+l[cur],c)+10
    ret3 = dfs(cur+1,a,b,c+l[cur])+10
    return min(ret0,ret1,ret2,ret3)

print(dfs(0,0,0,0))
