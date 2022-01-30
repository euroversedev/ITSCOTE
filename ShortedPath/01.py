import heapq

''' [문제] 전보 '''

N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [int(1e9)] * (N+1)


''' 다익스트라 알고리즘
1. 매 반복마다 가장 작은 최단거리를 가진 노드를 선택해서 => 힙 사용
2. 인접한 노드들에 대해 최단 거리 갱신
'''
def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0
    
    while h:
        dist, now = heapq.heappop(h)
        
        if visited[now] == True: continue
        else: visited[now] = True
        
        for vertex_num, edge_w in graph[now]:
            cost = dist + edge_w
            
            if cost < distance[vertex_num]:
                distance[vertex_num] = cost
                heapq.heappush(h, (cost, vertex_num))

for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))

dijkstra(start)
distance = set(distance)
distance.remove(int(1e9))
print(sum(visited) - 1, max(distance))