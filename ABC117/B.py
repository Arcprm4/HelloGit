import math
import collections
import itertools
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
MOD = 10**9+7

n = INT()
l = MAP()

m = max(l)
l.remove(m)
if m<sum(l):
    print("Yes")
else:
    print("No")