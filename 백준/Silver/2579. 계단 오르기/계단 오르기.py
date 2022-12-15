n = int(input())
S = [int(input()) for _ in range(n)]
dp = [0] * n

if n < 3:
    print(sum(S))
else:
    dp[0] = S[0]
    dp[1] = int(S[0] + S[1])
    dp[2] = max(S[0] + S[2], S[1] + S[2])
    for i in range(3, n):
        dp[i] = max(dp[i-2]+S[i], dp[i-3]+S[i-1]+S[i])
    print(dp[-1])