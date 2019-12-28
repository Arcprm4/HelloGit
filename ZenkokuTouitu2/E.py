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

L,N,M = map(int,input().split())

seki = list(map(int,input().split()))
sushi = list(map(int,input().split()))
flag = [False]*L
for i in seki:
    flag[i-1] = True

cnt=0
while 1:
    print(sushi)
    print(flag)
    for i in sushi:
        if (i in seki) and flag[i-1]==True:
            sushi.remove(i)
            flag[i-1] = 10

    if len(sushi)==0:
        break
    for i in range(len(sushi)):
        sushi[i] = (sushi[i]+1)%L


    for i in range(L):
        if flag[i]>=10:
            flag[i]+=1
        if flag[i]==20:
            flag[i] = True
    cnt+=1

print(cnt+10)