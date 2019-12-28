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

n,m = MAP()
a = MAP()
a = [-i for i in a]
heapify(a)
for i in range(m):
    tmp = -heappop(a)
    heappush(a,-(tmp//2))
print(-sum(a))