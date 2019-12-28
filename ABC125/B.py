def MAP(): return map(int,input().split())

n = int(input())
*v, = MAP()
*c, = MAP()

ans=0
for i in range(n):
    if v[i]-c[i]>0:
        ans+=v[i]-c[i]
print(ans)