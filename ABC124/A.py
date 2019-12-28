def MAP(): return map(int,input().split())

a,b = MAP()
ans=0
if a>b:
    ans+=a
    a-=1
    print(ans+max(a,b))
else:
    ans+=b
    b-=1
    print(ans+max(a,b))
