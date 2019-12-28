import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush,heapify
sys.setrecursionlimit(10**6)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 998244353

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

n = INT()
a = MAP()
ans=0

for i in range(n-1):
    for j in range(i+1,n):
        ans+=lcm(a[i],a[j])
    ans%=MOD

print(ans)
