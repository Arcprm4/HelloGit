import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush,heapify
sys.setrecursionlimit(10**7)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7

def cmb(n, r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

n,k = MAP()

for i in range(1,k+1):
    try:
        print(cmb(n-k+1,i)*cmb(k-1,i-1)%MOD)
    except:
        print(0)

