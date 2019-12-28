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

s = input()
t = input()
n = len(s)
m = len(t)

pre = [[0]*(m+1) for _ in range(n+1)]
dp = [[0]*(m+1) for _ in range(n+1)]

for si in range(n):
    for ti in range(m):
        if s[si]==t[ti]:
            dp[si+1][ti+1] = dp[si][ti]+1
        else:
            dp[si+1][ti+1] = max(dp[si+1][ti],dp[si][ti+1])

ans = ""
x = dp[-1][-1]
for i in range(n,-1,-1):
    for j in range(m,-1,-1):
        if dp[i][j]==x:
            if (dp[i-1][j]==x-1) and (dp[i][j-1]==x-1):
                ans = s[i-1]+ans
                x-=1
                break
print(ans)
