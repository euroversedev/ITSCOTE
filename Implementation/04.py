''' [문제] 문자열 재정렬 '''

s = input()

chr = []
sum = 0
for i in range(len(s)):
    if ord('0')<=ord(s[i])<=ord('9'): sum += int(s[i])
    else: chr.append(s[i])

sorted_s = sorted(chr)
print(''.join(sorted_s) + str(sum))
