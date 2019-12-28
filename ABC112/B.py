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
INF = 10**9

n,T = MAP()
ans = INF
for i in range(n):
    c,t = MAP()
    if t<=T:
        ans = min(c,ans)
if ans==INF:
    print("TLE")
else:
    print(ans)