import fractions
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import functools

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

def lcm_base(x,y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return functools.reduce(lcm_base, numbers, 1)

n,m = LI()
a = LI()

lcm = a[0]
for i in range(1,n):
    lcm = lcm * a[i] // fractions.gcd(lcm,a[i])
print((m//(lcm//2))-(m//lcm))
