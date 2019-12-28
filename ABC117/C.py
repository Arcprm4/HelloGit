import math
import collections
import itertools
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
MOD = 10**9+7

n,m = MAP()
x = MAP()
x.sort()

if n>=m:
    print(0)
    exit(0)

ll = []
for i in range(m-1):
    ll.append(x[i+1]-x[i])
ll.sort()
print(sum(ll[0:max(0, m - n)]))