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

m = INT()
ll = []
for i in range(m):
    tmp = MAP()
    ll += [tmp[0]]*tmp[1]

cnt=0
while len(ll)!=1:
    tmp = ll[0] + ll[1]
    del ll[0:2]
    if tmp>=10:
        ll.insert(0,tmp-10)
        ll.insert(0,tmp//10)
    else:
        ll.insert(0,tmp)
    cnt+=1

print(cnt)