import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush,heapify
import numpy as np
sys.setrecursionlimit(10**6)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7

n,k = MAP()
a = np.array(MAP())
f = np.array(MAP())

a = np.sort(a)
f = np.sort(f)[::-1]
l = 0
r = 10 ** 12

while l <= r:
    m = (l + r) // 2
    print(np.clip(a - m // f, 0, None))
    req = np.clip(a - m // f, 0, None).sum()
    if req > k:
        l = m + 1
    else:
        r = m - 1
print(l)

