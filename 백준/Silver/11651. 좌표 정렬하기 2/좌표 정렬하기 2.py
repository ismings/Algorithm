import sys
l = []
for _ in range(int(sys.stdin.readline())):
    b,a  = map(int, sys.stdin.readline().split())
    l.append([a, b])
for a,b in sorted(l):
    print(b,a)