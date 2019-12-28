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

def dist(l1,l2):
    return math.sqrt((l1[0]-l2[0])**2 + (l1[1]-l2[1])**2)

n = INT()
ll = [MAP() for _ in range(n)]

ans=0
for i in itertools.permutations(ll):
    for j in range(n-1):
        ans += dist(i[j],i[j+1])

print(ans/math.factorial(n))