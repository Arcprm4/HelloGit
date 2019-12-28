n,k = map(int,input().split())
*a, = map(int,input().split())
mod = 10**9+7

mae=0
ato=0
ans=0
sum = (k*(k-1))//2
for i in range(n):
    mae, ato = 0, 0
    for j in range(n):
        if a[i]>a[j]:
            if i<j:
                ato+=1
            else:
                mae+=1
    ans += (sum)*(mae+ato) + (ato*k)
    ans%=mod

print(ans)