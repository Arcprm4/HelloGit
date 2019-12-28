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
MOD = 998244353


n = INT()
d = MAP()

if d[0]!=0 or not all(d[1:]):
    print(0)
    exit(0)

l = [0]*(max(d)+1)
for i in d:
    l[i]+=1

ans=1
for i in range(1,max(d)+1):
    ans*=pow(l[i-1],l[i],MOD)
    ans %= MOD
print(ans)