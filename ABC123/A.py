def MAP(): return map(int,input().split())

p = [int(input()) for _ in range(5)]
k = int(input())
ans=0

for i in range(3):
    for j in range(i+1,5):
        if abs(p[i]-p[j])>k:
            flag=False
            print(":(")
            exit(0)

print("Yay!")