from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
city = [i for i in range(n)]
W = [list(map(int,input().split())) for _ in range(n)]
res = sys.maxsize

for p in permutations(city, n):
    if W[p[-1]][p[0]] == 0: continue
    cost = 0
    flag = True
    for i in range(1,n):
        if W[p[i-1]][p[i]] == 0:
            flag = False
            break
        cost += W[p[i-1]][p[i]]
        if cost >= res:
            flag = False
            break
    if flag:
        cost += W[p[-1]][p[0]]
        res = min(res, cost)

print(res)