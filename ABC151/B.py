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

n,k,m = LI()
a = LI()

if n*m-(sum(a))<=k:
    print(max(n*m-(sum(a)),0))
else:
    print(-1)
