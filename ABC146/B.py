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
s = input()

for i in s:
    ch = (ord(i) - ord("A") + n)%26 + ord("A")
    print(chr(ch),end="")
print()