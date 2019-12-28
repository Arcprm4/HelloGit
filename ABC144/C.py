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

res=1
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        res=i

print(res+(n//res)-2)