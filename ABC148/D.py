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
a = MAP()

if not 1 in a:
    print(-1)
    exit(0)


serch = 1
ans=0
for i in a:
    if i==serch:
        serch+=1
    else:
        ans+=1
print(ans)