''' [문제] 1로 만들기 '''

X = int(input())
dp = [0] * (X+1)

dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[5] = 1
for i in range(1, X+1):    # 1부터 X까지
    array = []
    if dp[i] == 0:    # 처리되지 않은 dp에 대하여,
        if i % 2 == 0: array.append(dp[i//2])
        if i % 3 == 0: array.append(dp[i//3])
        if i % 5 == 0: array.append(dp[i//5])
        array.append(dp[i-1])
        dp[i] = min(array) + 1

print(dp[X])