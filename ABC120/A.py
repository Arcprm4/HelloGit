def MAP(): return list(map(int,input().split()))

a,b,c = MAP()
print(min(b//a,c))