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

n,m = MAP()
a = MAP()
b = MAP()

res = [0]*(max(a)+max(b)+1)
for i,x in enumerate(a):
    for j,y in enumerate(b):
        if res[x+y]!=0:
            v,w = res[x+y]
            print(v,w,i,j)
            exit(0)
        else:
            res[x+y] = (i,j)

print(-1)