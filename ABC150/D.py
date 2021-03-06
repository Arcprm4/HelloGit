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
a = [int(i)//2 for i in LI()]

def num_of_2(x):
    c = 0
    while x%2==0:
        c+=1
        x//=2
    return c

a0 = num_of_2(a[0])
if any([num_of_2(i) != a0 for i in a]):
    print(0)
else:
    def lcm(x,y):
        return x//fractions.gcd(x,y)*y

    c = 1
    for i in a:
        c = lcm(c,i)
        if c>=inf:
            break
    
    ans = m//c
    print((ans+1)//2)
