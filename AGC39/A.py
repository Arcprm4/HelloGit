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
k = INT()
n = len(s)

if len(set(list(s)))==1:
    print(n*k//2)
    exit()

l=[]
tmp=1
ans=0
for i in range(1,n):
    if s[i-1]==s[i]:
        tmp+=1
    else:
        l.append(tmp)
        tmp=1
l.append(tmp)
for i in l:
    ans+=i//2
ans*=k

if s[0]==s[-1]:
    a = l[0]
    b = l[-1]
    res = (a//2) + (b//2) - ((a+b)//2)
    print(ans-(res*(k-1)))
else:
    print(ans)
