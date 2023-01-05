n = int(input())
line = sorted(list(map(int,input().split())))
ans = 0
for i in range(1,n+1):
    ans += sum(line[:i])
print(ans)