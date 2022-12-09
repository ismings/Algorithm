import sys
a = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
for ele in sorted(a):
    print(ele)
