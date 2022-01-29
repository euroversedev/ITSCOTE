''' [문제] 시각 '''

N = int(input())
count = 0

h = list(range(N + 1))
m = list(range(60))
s = list(range(60))

array = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36,
        37, 38, 39, 43, 53]

for i in h:
    for j in m:
        for k in s:
            if (i in array) or (j in array) or (k in array): count += 1
print(count)

''' [review]
시간 안에 해결 가능해보여서 완전 탐색(브루트포스)로 풀었음.

array에 3이 포함된 숫자를 저장할 필요없이,
if '3' in str(i)+str(j)+str(k): count += 1
이렇게 하면 3이 포함된 경우를 모두 검사할 수 있음.
'''