import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import copy

sys.setrecursionlimit(10**9)
mod = 998244353
inf = 10**20

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
"""
H,N = LI()
A = []
B = []
for i in range(N):
    a,b = LI()
    A.append(a)
    B.append(b)

dp = [inf]*(H+1)
ans = inf

dp[H] = 0

for i in range(N):
    for h in range(H+1)[::-1]:
        dp[h] = min(dp[h],dp[min(H,h+A[i])]+B[i])
print(dp[0])
"""

n = int(input())

l = ["a","b","c","d","e"]
for i in range(1,n+1):
    tmp = ""
    for j in range(2,7):
        if i%j==0:
            tmp += l[j-2]
    if len(tmp)==0:
        print(i)
    else:
	    print(tmp)



