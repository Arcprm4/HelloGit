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
MOD = 10**9+7


n, m = MAP()
a = MAP()
p = [(a[i], 1) for i in range(n)]
for j in range(m):
    b, c = MAP()
    p.append((c, b))
p.sort(reverse=True)
print(p)
ans, cnt = 0, n
for (v, c) in p:
    use = min(c, cnt)
    ans += use * v
    cnt -= use
print(ans)