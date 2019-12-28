def MAP(): return map(int,input().split())

n,q = MAP()
s = input()
t = [0]*(n+1)
for i in range(n):
    t[i+1] = t[i]+(1 if s[i:i+2]=="AC" else 0)
print(t)
for i in range(q):
    l,r = MAP()
    print(t[r-1]-t[l-1])