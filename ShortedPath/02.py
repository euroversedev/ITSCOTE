''' [문제] 미래 도시 '''

N, M = map(int, input().split())
graph = [[int(1e9)] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b: graph[a][b] = 0

X, K = map(int, input().split())
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


print(graph[1][K]+graph[K][X])
            

''' [review]
1. 노드의 갯수가 적고
2. A에서 K로, K에서 X로 가는 최소 이동 시간 = 다익스트라로 하면 각각 구해야함

위 두 가지 상황에 비춰보았을 때
모든 노드에서 모든 노드로 가는 최단거리를 구할 수 있는 플로이드 워셜 알고리즘이 적합.
'''