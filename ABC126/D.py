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


N = INT()
G = [dict() for _ in range(N)]
for i in range(N-1):
    u,v,w=map(int,input().split())
    G[u-1][v-1]=w
    G[v-1][u-1]=w
color=[-1 for _ in range(N)]
dist=[-1 for _ in range(N)]
dist[0]=0
q=[0]
while q:
    r=q.pop()
    print(G[r])
    for p in G[r]:
        print(p)
        if dist[p]!=-1:
            continue
        dist[p]=dist[r]+G[r][p]
        q.append(p)
for i in range(N):
    color[i]=dist[i]%2
for ans in color:
    print(ans)