def MAP(): return map(int,input().split())
s = input()
ans_1, ans_2= 0,0
for i,v in enumerate(s):
    if (i%2==0) and (v!="0"):
        ans_1+=1
    elif (i%2==1) and (v!="1"):
        ans_1+=1

for i,v in enumerate(s):
    if (i%2==0) and (v!="1"):
        ans_2+=1
    elif (i%2==1) and (v!="0"):
        ans_2+=1

print(min(ans_1,ans_2))
