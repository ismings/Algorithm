n = int(input())
dp = [[0]*10 for _ in range(n+1)]
dp[0] = [1]*10

for i in range(1,n):
    total = sum(dp[i-1])
    for j in range(10):
        if j != 0:
            total -= dp[i-1][j-1]
        dp[i][j] = total

print(sum(dp[n-1]) % 10007)