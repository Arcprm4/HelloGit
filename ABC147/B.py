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

s = list(input())
n = len(s)
if n%2==0:
    l = s[0:len(s)//2]
    r = s[len(s)//2:len(s)]
else:
    l = s[0:n//2]
    r = s[n//2+1:n]

r.reverse()
ans=0
for i in range(n//2):
    if l[i]!=r[i]:
        ans+=1

print(ans)