from collections import deque
''' [문제] 미로 탈출 '''

N, M = map(int, input().split())
array = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

ds = [(+1, 0), (-1, 0), (0, +1), (0, -1)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))    # 시작 노드를 큐에 삽입
    
    while queue:
        now = queue.popleft()    # x = now[0], y = now[1]
        for dx, dy in ds:        # 모든 인접 노드에 대하여
            if 0<=now[0]+dx<N and 0<=now[1]+dy<M:
                if visited[now[0]+dx][now[1]+dy] == False:
                    queue.append((now[0]+dx, now[1]+dy))
                    visited[now[0]+dx][now[1]+dy] = True
                    array[now[0]+dx][now[1]+dy] = array[now[0]][now[1]] + 1    
                
bfs(0, 0)
print(array[N-1][M-1])

''' [review]
잘못된 풀이 : 최소 이동 칸수 = 최단 경로 = 스택(재귀) 깊이로 구할 수 있음
옳은 풀이 : 최단 거리&경로 => BFS 사용해서 각 지점까지의 최단 거리 기록

DFS를 이용한 잘못된 풀이를 할 경우
=> 시작점에서 도착점으로 가는 거의 무한한 종류의 길을 모두 탐색하게 됨.
반면 BFS는 도착점에 도달한 순간 끝남.

* 행렬 다룰때 x가 뭔지 y가 뭔지 분명히 인지하고 써야할 듯
array[x][y] => x번째 줄 y번 째 원소 => x를 세로, y를 가로로 인지하자
=> 0<=x+dx<N and 0<=y+dy<M
'''