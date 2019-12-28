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

N,W = MAP()
weight=[]
value=[]
for i in range(N):
    w,v = MAP()
    weight.append(w)
    value.append(v)
MAX_V = 100100

dp = [[MOD]*(MAX_V+1) for _ in range(N+1)]
dp[0][0]=0

for i in range(N):
    for sum_v in range(MAX_V):
        if sum_v - value[i]>=0:
            dp[i+1][sum_v] = min(dp[i+1][sum_v],dp[i][sum_v-value[i]]+weight[i])
        dp[i+1][sum_v] = min(dp[i+1][sum_v],dp[i][sum_v])


for sum_v in range(MAX_V):
    if dp[N][sum_v]<=W:
        res=sum_v
print(res)