import math
 
def jud(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
 
n = int(input())
while 1:
    if jud(n):
        print(n)
        exit()
    n+=1