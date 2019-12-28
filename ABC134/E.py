n = int(input())
*a, = map(int,input().split())
box = [0]*n
for i in range(n,0,-1):
    sum_box = 0
    for j in range(i,n+1,i):
        sum_box+=box[j-1]
    if sum_box%2!=a[i-1]:
        box[i-1]+=1

print(sum(box))
if sum(box):
    ans = []
    for i, x in enumerate(box):
        if x:
            ans.append(i+1)
    print(*ans)