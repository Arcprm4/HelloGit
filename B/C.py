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

n,l,x = MAP()
res = [x]

for i in range(n):
    tmp = INT()
    if tmp in res:
        res.remove(tmp)
    else:
        res.append(tmp)
    res_ = sorted([min(i,l-i) for i in res])
    res_ = sorted([l-x if i%2 else x for i,x in enumerate(res_)])
    print(min(abs(res_[i]-res_[i+1]) for i in range(len(res_)-1)))

