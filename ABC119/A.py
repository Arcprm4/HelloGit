def MAP(): return list(map(int,input().split("/")))

y,m,d = MAP()
if y<2019:
    print("Heisei")
elif y>2019:
    print("TBD")
elif m<=4:
    print("Heisei")
else:
    print("TBD")