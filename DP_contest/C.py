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
a = [MAP() for _ in range(n)]
dp = [[0,0,0] for _ in range(n+1)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j==k:
                continue
            dp[i+1][k] = max(dp[i+1][k],dp[i][j]+a[i][k])

print(max(dp[n]))