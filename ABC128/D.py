def MAP(): return map(int,input().split())

n,k = MAP()
*v, = MAP()

operation = min(n,k) #取り出すMAX回数
ans=0

for i in range(1,operation+1):
    for j in range(i+1):
        A = j   #左側から取り出す回数
        B = i-j    #右側から取り出す回数
        t = v[:A]
        if B>0:
            t+=v[-B:]
        t.sort()

        l = min(k-i,i-1)
        for ll in range(l):
            if t[ll] >= 0:
                l = ll
                break
        s = sum(t[l:])
        ans = max(ans,s)

print(ans)


