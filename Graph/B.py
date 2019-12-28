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

W,H = MAP()
field = [MAP() for _ in range(H)]

def dfs(h,w):
    field[h][w] = 0

    for dh in range(-1,2):
        for dw in range(-1,2):
            nh = h + dh
            nw = w + dw

            if (nh<0) or (nh>=H) or (nw<0) or (nw>=W):
                continue
            if field[nh][nw] == 0:
                continue
            dfs(nh,nw)

cnt=0
for i in range(H):
    for j in range(W):
        if field[i][j]==0:
            continue
        dfs(i,j)
        cnt+=1

print(cnt)