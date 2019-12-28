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


n = int(input())
G = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    G[a].append([b,i])

ans = [None]*(n-1)
def rec(cur,color):

    cnt = 1
    for (to, j) in G[cur]:
        if cnt == color:
            cnt += 1
        ans[j] = cnt
        rec(to, cnt)
        cnt += 1
rec(0, 0)
print(max(ans))
print(*ans, sep="\n")
