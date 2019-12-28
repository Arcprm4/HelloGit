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

n,k = MAP()
h = [INT() for _ in range(n)]
h.sort()
print(min(h[i+k-1]-h[i] for i in range(n-k+1)))