import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys

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



n = I()
ans=0
c = [[0]*10 for i in range(10)]

for i in range(1,n+1):
    s = str(i)
    if s[0]=="0" or s[-1]=="0":
        continue
    c[int(s[0])][int(s[-1])]+=1


for i in range(1,10):
    for j in range(1,10):
        ans+=c[i][j]*c[j][i]
print(ans)

