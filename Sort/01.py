''' [문제] 두 배열의 원소 교체 '''

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

for i in range(K):
    A[i], B[-1-i] = B[-1-i], A[i]
print(sum(A))
