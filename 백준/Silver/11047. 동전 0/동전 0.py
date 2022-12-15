n, money = map(int, input().split())
lst = [int(input()) for _ in range(n)]
cnt = 0
for m in lst[::-1]:
    share = money // m
    if share > 0:
        money -= m * share
        cnt += share
print(cnt)