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
h = MAP()

dp = [MOD]*n
dp[0]=0

for i in range(n-1):
    dp[i+1] = min(dp[i+1],dp[i]+abs(h[i]-h[i+1]))
    if i<n-2:
        dp[i+2] = min(dp[i+2],dp[i]+abs(h[i]-h[i+2]))

print(dp[n-1])