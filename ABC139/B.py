def MAP(): return map(int,input().split())
import math

a,b = MAP()
print(math.ceil((b-a)/(a-1))+1)