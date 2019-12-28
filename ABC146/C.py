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


a,b,x = MAP()

ans=0
for i in range(1,18):
    if b*i > x:
        continue
    lower = 10**(i-1)
    upper = 10**i
    n = (x-(b*i))//a
    if n < upper:
        ans = max(ans,n)
ans = min(ans,10**9)
print(ans)