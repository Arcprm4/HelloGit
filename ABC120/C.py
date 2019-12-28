def MAP(): return list(map(int,input().split()))

s = list(input())

print(min(s.count("0"),s.count("1"))*2)