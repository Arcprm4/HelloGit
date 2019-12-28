def MAP(): return list(map(int,input().split()))
"""
#排他的論理和
def XOR(lst):
    #lst = [000,010,011...] type is str
    lst = sorted(lst,key = lambda x:len(x),reverse = True)
    n = len(lst[0])
    ans = []
    for i in range(1,n+1):
        tmp = 0
        for j in lst:
            if len(j)>=i:
                if j[-i]=="1":
                    tmp+=1
        if tmp%2==0:
            ans.insert(0,"0")
        else:
            ans.insert(0,"1")
    return "".join(ans)

#10進数→2進数
def binary(num):
    lst = []
    while num!=0:
        lst.insert(0,num%2)
        num = num//2
    return "".join(map(str,lst))

#2進数→10進数
def decimal(num):
    ans=0
    for i,x in enumerate(str(num)[::-1]):
        ans += int(x)*2**i
    return ans
"""
def f(x):
    tmp = (x+1)%4
    if tmp==0:
        return 0
    elif tmp==1:
        return x
    elif tmp==2:
        return 1
    else:
        return 1^x
A,B = MAP()
print(f(A-1)^f(B))