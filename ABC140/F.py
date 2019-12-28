def MAP(): return list(map(int,input().split()))
import collections

n = int(input())
s = MAP()
st = collections.defaultdict(int)
for i in s:
    st[i] += 1

for i in range(n):
    
