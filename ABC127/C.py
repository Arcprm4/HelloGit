import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush
sys.setrecursionlimit(10**6)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7

n,m = MAP()
l,r = [], []
for i in range(m):
    a,b = MAP()
    l.append(a)
    r.append(b)

max_l = max(l)
min_r = min(r)
if min_r<max_l:
    print(0)
    exit()
print(min_r-max_l+1)