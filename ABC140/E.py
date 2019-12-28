def MAP(): return list(map(int,input().split()))

n = int(input())
p = MAP()

ans=0
for i in range(n-1):
    tmp = p[i:n]
    a = sorted(tmp,reverse=True)[0]
    b = sorted(tmp,reverse=True)[1]
    
print(ans)
