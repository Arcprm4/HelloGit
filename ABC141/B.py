import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush
sys.setrecursionlimit(10**6)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7

s = input()
odd = ["R","U","D"]
even = ["L","U","D"]
flag1=True
flag2=True
for i in range(1,len(s)+1):
    if (i%2==1) and not(s[i-1] in odd):
        flag1 =False
    if (i%2==0) and not(s[i-1] in even):
        flag2 = False

if flag1 and flag2:
    print("Yes")
else:
    print("No")