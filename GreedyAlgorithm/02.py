''' [문제] 곱하기 혹은 더하기 '''

S = input()

result = 0
array = [0, 1]
for i in range(len(S)):
    k = int(S[i])
    if (result in array) or (k in array):
        result += k
    else: result = result * k

print(result)

''' [review]
array에 0과 1 넣을 필요없이
그냥 result <= 1 or k <= 1 이렇게 하면 됨.
'''