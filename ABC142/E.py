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

N,M = MAP()
A=[]
B=[]
C=[]
for i in range(M):
    a,b = MAP()
    A.append(a)
    B.append(b)
    C.append(MAP())

print(A,B,C)
