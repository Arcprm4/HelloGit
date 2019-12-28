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

n=INT()
res = [0]*10**5

ans=0
for i in range(n):
    tmp = INT()
    res[tmp] += 1
    if res[tmp] > 1:
        ans+=1

print(ans)