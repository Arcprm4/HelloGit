def MAP(): return map(int,input().split())
import math

n = int(input())
points = [list(MAP()) for _ in range(n)]
plus=[0,0]
minus=[0,0]

for i in points:
    if sum(i)>0:
        plus[0] += i[0]
        plus[1] += i[1]
    else:
        minus[0] += i[0]
        minus[1] += i[1]

print(max( math.sqrt(plus[0]**2+plus[1]**2), math.sqrt(minus[0]**2+minus[1]**2) ))