def MAP(): return map(int,input().split())
def gcd(a, b):
    while b:
        a %= b
        a, b = b, a
    return a

n = int(input())
*a, = MAP()

x=[0 for _ in range(n)]
y=[0 for _ in range(n)]
for i in range(1,n):
    x[i]=gcd(x[i-1],a[i-1])
for i in range(n-1)[::-1]:
    y[i]=gcd(y[i+1],a[i+1])
Z=[gcd(x[i],y[i]) for i in range(n)]
print(max(Z))