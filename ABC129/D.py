def MAP(): return map(int,input().split())
#Python3 -> can't pass,but Pypy3 -< pass
H,W = MAP()
lst = [list(input()) for _ in range(H)]
L = [[0 for _ in range(W)] for _ in range(H)]
R = [[0 for _ in range(W)] for _ in range(H)]
D = [[0 for _ in range(W)] for _ in range(H)]
U = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        #Left
        if lst[i][j]==".":
            L[i][j] = L[i][j-1]+1
        #Up
            U[i][j] = U[i-1][j]+1
        #Right
        if lst[i][-(j+1)]==".":
            R[i][-(j+1)] = R[i][-j]+1
        #Down
        if lst[-(i+1)][j]==".":
            D[-(i+1)][j] = D[-i][j]+1
ans=0
for i in range(H):
    for j in range(W):
        ans = max(ans,L[i][j]+R[i][j]+U[i][j]+D[i][j]-3)
print(ans)