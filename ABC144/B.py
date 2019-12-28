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
flag = False
for i in range(1,10):
    if n%i==0:
        if 1 <= n//i <= 9:
            flag=True

if flag:
    print("Yes")
else:
    print("No")