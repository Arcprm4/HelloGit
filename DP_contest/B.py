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
h = MAP()

dp = [MOD]*n
dp[0]=0

for i in range(n-1):
    for j in range(i+1,min(i+k+1,n)):
        dp[j] = min(dp[j],dp[i]+abs(h[i]-h[j]))
print(dp[n-1])