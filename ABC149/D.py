import math
 
n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()
 
def h(x):
    if x=="r":
        return p
    if x=="p":
        return s
    return r
 
ans=0
for i in range(k):
    l = [t[j] for j in range(i,n,k)]
    #print(l)
    m = len(l)
    tmp = 0
    cnt=1
    for j in range(m-1):
        if l[j]==l[j+1]:
            cnt+=1
        else:
            tmp+=math.ceil(cnt/2)*h(l[j])
            cnt=1
    tmp+=math.ceil(cnt/2)*h(l[m-1])
    #print(tmp)
    ans+=tmp
print(ans)