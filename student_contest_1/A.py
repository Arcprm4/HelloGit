m,d = map(int,input().split())

ans=0
for i in range(1,m+1):
    for j in range(1,d+1):
        d_1 = j%10
        d_10 = (j-(j%10))//10
        if (d_1>=2) and (d_10>=2) and (d_1*d_10==i):
            ans+=1

print(ans)