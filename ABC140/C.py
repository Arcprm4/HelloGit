def MAP(): return list(map(int,input().split()))

n = int(input())
b = MAP()

a = [0]*n
a[0] = b[0]
a[n-1] = b[n-2]

for i in range(n-2):
    a[i+1] = min(b[i],b[i+1])
print(sum(a))