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
unhappy=0
if s[0]=="L":
    unhappy+=1
if s[n-1]=="R":
    unhappy+=1

for i in range(n-1):
    if s[i:i+2]=="RL":
        unhappy+=2
print(n-max(1,unhappy-(2*k)))