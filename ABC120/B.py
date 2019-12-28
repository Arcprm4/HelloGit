def MAP(): return list(map(int,input().split()))

a,b,k = MAP()
ans = [i for i in range(1,min(a+1,b+1)) if (a%i==0) and (b%i==0)]
print(ans[-k])
