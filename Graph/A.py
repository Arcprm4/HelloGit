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

H,W = MAP()
ll = [input() for _ in range(H)]
seen = [[False]*W for _ in range(H)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(h,w):
    seen[h][w] = True

    for i in range(4):
        nh = h + dx[i]
        nw = w + dy[i]

        if (nh<0) or (nh>=H) or (nw<0) or (nw>=W):
            continue
        if ll[nh][nw]=="#":
            continue
        if seen[nh][nw]:
            continue
        dfs(nh,nw)

for i in range(H):
    for j in range(W):
        if ll[i][j]=="s":
            sh = i
            sw = j
        if ll[i][j]=="g":
            gh = i
            gw = j

dfs(sh,sw)
if seen[gh][gw]:
    print("Yes")
else:
    print("No")