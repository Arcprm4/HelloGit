def MAP(): return list(map(int,input().split()))

n,m = MAP()
lst = [MAP() for _ in range(n)]
lst = sorted(lst,key = lambda x:x[0])
q = 0
ans = 0

for i in lst:
    if q+i[1]<m:
        q+=i[1]
        ans+=i[0]*i[1]
    else:
        ans += (m-q)*i[0]
        break

print(ans)