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


n,k = MAP()
s = input()
k*=2

lst = [0]
for i in range(n-1):
    if s[i]!=s[i+1]:
        lst.append(i+1)

r = len(lst)
lst += [n]
ans=[]
for i in range(r):
    if s[lst[i]]=="0":
        ans.append(lst[min(i+k,r)] - lst[i])
    else:
        ans.append(lst[min(i+k+1,r)] - lst[i])

print(max(ans))