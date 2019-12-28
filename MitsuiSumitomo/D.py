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
s = input()

l = []
ans=0
for i in itertools.combinations(s,3):
    if not i in l:
        ans+=1
        l.append(i)
print(ans)