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

N,M = MAP()
Y = [0]*(10**5)
P = [0]*(10**5)
yd =[[] for _ in range(N)]
for i in range(M):
    p,y = MAP()
    P[i] = p-1
    Y[i] = y
    yd[p-1].append(y)

for i in range(N):
    yd[i].sort()

for i in range(M):
    print("{0:06d}".format(P[i]+1),end="")
    print("{0:06d}".format(bisect.bisect_left(yd[P[i]],Y[i])+1))

