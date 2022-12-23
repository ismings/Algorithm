import sys
from collections import defaultdict
input = sys.stdin.readline
dict = defaultdict(int)
for _ in range(int(input())):
    dict[int(input())] += 1

maxnum = max(dict.values())
print(sorted([k for k,v in dict.items() if maxnum == v])[0])