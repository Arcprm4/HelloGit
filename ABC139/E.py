def MAP(): return list(map(int,input().split()))
import collections

n = int(input())
a = [MAP() for _ in range(n)]
q = list(range(n))
c = collections.defaultdict(int)
t = [0]*n
r=0

while q:
    r += 1
    nq = []
    for i in q:
        j = a[i][t[i]]-1
        k = i
        if k<j:
            j,k = k,j
        c[(j,k)] += 1
        if c[(j,k)] == 2:
            t[j] += 1
            t[k] += 1
            if t[j] < n-1:
                nq.append(j)
            if t[k] < n-1:
                nq.append(k)
    q = nq

for tt in t:
    if tt!=n-1:
        print(-1)
        exit(0)
print(r)
