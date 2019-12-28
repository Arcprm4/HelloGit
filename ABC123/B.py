def MAP(): return map(int,input().split())

menu = [int(input()) for _ in range(5)]
menu = sorted(menu,key = lambda x:x%10)
flag = True
ans=0

for v in menu:
    if flag and v%10!=0:
        ans+=v
        flag=False
    else:
        if flag:
            ans+=v
        else:
            ans+= v + 10-(v%10)
print(ans)