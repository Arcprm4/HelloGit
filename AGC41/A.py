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

n,a,b = MAP()

if (b-a)%2==0:
    print((b-a)//2)
else:
    print(min(n-a,b-1)-((b-a)//2))
