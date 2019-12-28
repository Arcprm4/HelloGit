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

d = INT()

if d==25:
    print("Christmas")
if d==24:
    print("Christmas Eve")
if d==23:
    print("Christmas Eve Eve")
if d==22:
    print("Christmas Eve Eve Eve")