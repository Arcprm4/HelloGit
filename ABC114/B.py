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

s = input()
ans=1000
for i in range(len(s)-2):
    ans = min(ans,abs(int(s[i:i+3])-753))

print(ans)