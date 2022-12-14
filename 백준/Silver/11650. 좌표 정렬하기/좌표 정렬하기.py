import sys
a = [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
for a,b in sorted(a):
    print(a,b)