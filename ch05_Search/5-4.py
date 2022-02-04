# p152 미로 탈출

from collections import deque

n, m = map(int, input().split())
maze = [0 for _ in range(n)]
for i in range(n):
    maze[i] = list(map(int, input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            if 0 <= a+dx[i] < n and 0 <= b+dy[i] < m:
                if maze[a+dx[i]][b+dy[i]] == 1 and not (a+dx[i] == 0 and b+dy[i] == 0):
                    queue.append((a+dx[i], b+dy[i]))
                    maze[a+dx[i]][b+dy[i]] = maze[a][b] + 1


bfs(0, 0)
print(maze[n - 1][m - 1])