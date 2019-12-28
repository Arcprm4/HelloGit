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

n = INT()
t,a = MAP()
h = MAP()

res = MOD
for i in range(n):
    tmp = abs(a-(t-(h[i]*0.006)))
    print(tmp)
    if res>tmp:
        res = tmp
        ans = i+1
print(ans)
