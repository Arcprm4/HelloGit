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


N,M,T = MAP()
A = MAP()

G = [[] for _ in range(n)]
for i in range(n-1):
    u,v = MAP()
    u,v = u-1,v-1
    G[u].append(v)
    G[v].append(u)

def dfs(v,p,d):
    for nv in G[v]:
        if nv==p:
            continue
        dfs(nv,v,d+1)

root = 0
dfs(root,-1)