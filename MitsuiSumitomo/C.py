import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush,heapify
sys.setrecursionlimit(10**9)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7

x = INT()

for i in range(1,10**6+1):
    if i*100<=x<=i*105:
        print(1)
        exit()
print(0)