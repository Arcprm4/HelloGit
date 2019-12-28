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
n = len(s)

l = [0]*(n+1)
cnt=0
for i in range(n):
    if s[i]=="<":
        cnt+=1
    else:
        cnt=0
    l[i+1] = cnt

for i in range(n)[::-1]:
    if s[i]==">":
        cnt+=1
    else:
        cnt=0
    l[i] = max(l[i],cnt)

print(sum(l))