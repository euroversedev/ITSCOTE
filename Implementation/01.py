''' [문제] 상하좌우 '''

N = int(input())
array = input().split()

x, y = 0, 0
for cmd in array:
    if cmd == 'U': y -= 1
    elif cmd == 'D': y += 1
    elif cmd == 'L': x -= 1
    elif cmd == 'R': x += 1
    
    if x < 0: x = 0
    if N < x: x = N - 1
    if y < 0: y = 0
    if N < y: y = N - 1
        
print(y+1, x+1)

''' [review]
https://youtu.be/puH2p1CQEg4?list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81
Implementation(구현)의 대표적인 유형인 시뮬레이션 문제입니다.

x와 y를 바로 이동하지 않고 임시로 nx, ny에 저장한 뒤에
0 < nx, ny < N 여부를 확인하고 x, y에 넣어주는 방식으로 하면 편함.
'''