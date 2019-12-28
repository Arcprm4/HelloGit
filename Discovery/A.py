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

def aa(num):
    if num==1:
        return 300000
    if num==2:
        return 200000
    if num==3:
        return 100000
    else:
        return 0
x,y = MAP()
ans=0
if x==1 and y==1:
    ans += 400000

ans += aa(x) + aa(y)
print(ans)
