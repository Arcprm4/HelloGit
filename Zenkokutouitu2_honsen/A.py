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
a = MAP()

ans = 0
for i in range(1,n-1):
    tmp = a[i]
    l = 0
    r = 0
    for j in a[:i]:
        if j<tmp:
            l+=1
    for j in a[i+1:]:
        if tmp>j:
            r+=1
    ans += l*r

print(ans)