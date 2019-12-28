import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush
sys.setrecursionlimit(10**6)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7

n,k,q = MAP()
lst = [0]*n
for i in range(q):
    lst[INT()-1]+=1

x = sum(lst)
for i in lst:
    if x-i>=k:
        print("No")
    else:
        print("Yes")