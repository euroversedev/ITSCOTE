''' [문제] 1이 될때까지 '''

N, K = map(int, input().split())

count = 0
while N != 1:
    if N % K == 0:
        N = N // K
    else:
        N = N - 1
    count += 1

print(count)


''' [ review ]
https://youtu.be/_TG0hVYJ6D8?list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81

내가 작성한 코드는 O(N)의 시간복잡도를 갖는데,
동빈님이 작성한 아래 코드는 O(logN)을 갖는다.

target = (n//k)*k
count += n - target
n = target

1을 여러번 뺄 필요없이
N이 K로 나누어 떨어지는 수 target을 구한다.
'''
