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


n = INT()
l = MAP()

l.sort()
ans=0
for i in range(n):
    for j in range(i+1,n):
        idx = bisect.bisect_left(l,l[i]+l[j])
        ans+=idx-j-1

print(ans)