def MAP(): return list(map(int,input().split()))
def decimal(num):
    ans=0
    for i,x in enumerate(str(num)[::-1]):
        ans += int(x)*2**i
    return ans

l = decimal(int(input()))
lst = list(range(2,l+1))
ans=0

while lst:
    tmp=0
    k = lst[0]
    for i in range(k//2):
        if i^(k-i)==k:
            tmp += 1
    tmp*=2
    if (k%2==0) and ((k//2)^(k//2)==k):
        tmp+=1
    while k<=l:
        lst.remove(k)
        ans+=tmp
        k*=2
    print(lst)
    print(ans)

print(ans+3)


