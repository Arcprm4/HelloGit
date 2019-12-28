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

n,t = MAP()
dp = [0] * 6005
ab = []
for i in range(n):
    ab.append(MAP())

ab.sort(key=lambda x: x[0])
for u in ab:
    for i in range(6004-u[0], -1, -1):
        if i < t:
            dp[i+u[0]] = max(dp[i+u[0]], dp[i] + u[1])
print(max(dp))