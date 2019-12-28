def MAP(): return list(map(int,input().split()))

H,W = MAP()
h,w = MAP()

print(H*W-(h*W+w*H)+h*w)