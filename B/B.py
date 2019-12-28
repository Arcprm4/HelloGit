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
a = []
b = []
for i in range(n):
    tmp = input()
    a.append([i for i,x in enumerate(tmp) if x=="1"])
for i in range(n):
    tmp = input()
    b.append([i for i,x in enumerate(tmp) if x=="0"])

ans = [["1"]*n for _ in range(n)]
for i in range(n):
    for j in b[i]:
        for k in a[i]:
            ans[k][j]="0"

for i in range(n):
    print("".join(ans[i]))
