# p259 미래 도시

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

x, k = map(int, input().split())

# 플로이드-워셜 알고리즘 사용
for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])
            graph[b][a] = min(graph[a][b], graph[b][a])

if graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])