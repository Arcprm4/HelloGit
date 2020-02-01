import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys

sys.setrecursionlimit(10**9)
mod = 10**9+7
inf = 10**20

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

H,W = map(int,input().split())

field = [input() for i in range(H)]
search = [[0]*W for i in range(H)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(h,w):
    search[h][w] = 1

    for i in range(4):
        nh = h+dx[i]
        nw = w+dy[i]
        if (nh<0) or (nw<0) or (nw>W-1) or (nh>H-1):
            continue
        if field[nh][nw]==".":
            continue
        if search[nh][nw]==1:
            continue
        dfs(nh,nw)

dfs(0,0)
print(search)