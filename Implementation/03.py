''' [문제] 왕실의 나이트 '''

s = input()    # 'c2'와 같이 입력됨

ds = [(-2, -1), (-1, -2), (+1, -2), (+2, -1),
     (-2, +1), (-1, +2), (+1, +2), (+2, +1)]

x = ord(s[0]) - ord('a') + 1
y = int(s[1])

count = 0
for dx, dy in ds:
    if 1<=x+dx<=8 and 1<=y+dy<=8: count += 1

print(count)

''' [review]
1. ordinal value, character, binary 함수
ord(문자) : 문자를 아스키 코드로 반환해준다. ord('A') => 65
chr(숫자) : 숫자에 맞는 아스키 코드를 반환한다. chr(65) => A
bin(숫자) : 숫자를 이진수로 반환

2. ds에 여러개의 값이 저장되어 있는 경우
dx와 dy로 각각 받아올 수도 있지만,
for d in ds: // d[0] d[1]과 같이 인덱스로도 사용 가능
'''