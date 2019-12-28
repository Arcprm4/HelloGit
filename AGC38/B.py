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

n,k = MAP()
p = MAP()
ans=0

for i in range(n-k+1):
    tmp = p[i:i+k]
    if (i-1)>=0:
        if min(tmp)<p[i-1]:
            ans+=1
    if i+k<=n-1:
        if max(tmp)>p[i+k]:
            ans+=1

print(max(1,ans))