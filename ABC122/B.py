s = input()
ACGT = ["A","C","G","T"]
ans=0

for i in range(len(s)):
    flag = True
    tmp=0
    for j in range(i,len(s)):
        if s[j] not in ACGT:
            flag = False
            break
        tmp += 1
    ans=max(ans,tmp)

print(ans)