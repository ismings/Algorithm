import itertools as iter
n = int(input())
A = list(map(int, input().split()))
ans = 0
for ele in list(iter.permutations(A,n)):
    sum = 0
    for j in range(n-1):
        sum += abs(ele[j] - ele[j+1])
    ans = max(ans, sum)

print(ans)