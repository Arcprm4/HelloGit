def MAP(): return map(int,input().split())
import math

n = int(input())
ls = [int(input()) for _ in range(5)]

print(math.ceil(n/min(ls))+4)