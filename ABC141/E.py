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

def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]

n = INT()
s = input()

a=0
i=0
j=1

while j<n:
    if s[i:j] in s[j:]:
        a = max(a,len(s[i:j]))
        j+=1
    else:
        i+=1
    if i==j:
        i+=1
        j+=2

print(a)