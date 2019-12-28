n,h,w = map(int,input().split())
matrix = [[[] for j in range(w)] for i in range(h)]

for i in range(n):
    r,c,a = map(int,input().split())
    matrix[r-1][c-1].append(a)
