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

a = INT()
b = INT()

l = [0]*3
l[a-1]=1
l[b-1]=1
print(l.index(0)+1)