def MAP(): return list(map(int,input().split()))
import fractions

n = int(input())
A = MAP()

tmp=A[0]
for i in range(1,n):
    tmp = fractions.gcd(tmp,A[i])
print(tmp)