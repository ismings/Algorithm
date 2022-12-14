import sys

n = int(sys.stdin.readline())
score = [list(sys.stdin.readline().split()) for _ in range(n)]
score.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for s in score:
    print(s[0])