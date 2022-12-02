n = int(input())
#n이 1일 경우, IndexError 발생
dp = [0] * 1000

dp[0], dp[1] = 1, 2
for i in range(2,1000):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n-1])