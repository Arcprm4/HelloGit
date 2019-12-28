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

#dp[i][sum_w]:=i-1番目の品物から重さがsum_wを超えないように選んだ時の価値の総和の最大
dp = [[0]*(W+1) for _ in range(N+1)]
for i in range(N):
    for sum_w in range(W+1):
        if sum_w-weight[i]>=0:
            dp[i+1][sum_w] = max(dp[i+1][sum_w],dp[i][sum_w-weight[i]]+value[i])
        
        dp[i+1][sum_w] = max(dp[i+1][sum_w],dp[i][sum_w])

print(dp)