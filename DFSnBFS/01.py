''' [문제] 음료수 얼려먹기 '''

N, M = map(int, input().split())
array = [list(map(int, list(input()))) for _ in range(N)]
dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]

def dfs(i, j):
    if array[i][j] == 0:    # 방문 노드 visited
        array[i][j] = 1
        
    for k in range(4):      # 인접 노드에 대해서 DFS
        if 0<=i+dx[k]<N and 0<=j+dy[k]<M:
            if array[i+dx[k]][j+dy[k]] == 0:
                dfs(i+dx[k], j+dy[k])
    
count = 0
for j in range(M):
    for i in range(N):
        if array[i][j] == 0:
            dfs(i, j)
            count += 1
print(count)
print(array)
        
''' [review]
DFS던 BFS던 사용해서 각각의 얼음 틀을 1로 채운다.

공백없이 입력된 문자열을 정수형 리스트로 저장하는 법
=> array = [list(map(int, input())) for _ in range(N)]
map(function, iterable) 함수는 리스트와 같이 iterable한 값을 인자로 받는다.
따라서, map(int, input())과 int(input())은 동일하지 않다.
map(int,input())은 list(input())의 각 요소에 int()를 적용하는 것과 같다.
'''