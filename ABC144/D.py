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

a,b,x = MAP()

res = (2*x)/(a*b)
if res<=a:
    print(math.degrees(math.atan(b/res)))
else:
    tmp = b - ((b/a)*(res-a))
    print(math.degrees(math.atan(tmp/a)))
