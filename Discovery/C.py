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

H,W,K = MAP()
ll = [list(input()) for _ in range(H)]
ans = [[0]*W for _ in range(H)]

cnt = 1
for i in range(H):
    for j in range(W):
        if ll[i][j]=="#":
            start_h = i
            end_h = i
            ans[i][j] = cnt
            for k in range(i,-1,-1): #上
                if ans[k][j]!=0:
                    start_h = k
                    break
                else:
                    ans[i][j] = cnt
            for k in range(i,H):
                if ans[k][j]!=0:
                    end_h = k
                    break
                else:
                    ans[i][j] = cnt
            
            
            cnt+=1

