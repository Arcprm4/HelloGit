def MAP(): return list(map(int,input().split()))

n,m,c = MAP()
b = MAP()
ans=0
for i in range(n):
    sm=0
    a = MAP()
    for j in range(m):
        sm += a[j]*b[j]
    if sm+c>0:
        ans+=1

print(ans)