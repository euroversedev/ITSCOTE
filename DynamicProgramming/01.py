''' [문제] 개미 전사 '''

N = int(input())
array = list(map(int, input().split()))

dp = [0] * N
dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + array[i])

print(max(dp[-1], dp[-2]))

''' [review]
DP 상향식 (바텀업)으로 풀이 가능

print에서 끝에서 두개를 비교했는데,
애초에 dp[-1]에 dp[-2]까지 고려한 최대 값이 저장되어 있기 때문에
print(dp[-1])로 하면됨.
'''