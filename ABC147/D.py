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

m = 1
ans=0
for _ in range(60):
    bit = sum(i & m for i in a)
    bit //= m
    non_bit = n-bit
    ans = (ans+bit*non_bit*m)%MOD
    m <<= 1
print(ans)