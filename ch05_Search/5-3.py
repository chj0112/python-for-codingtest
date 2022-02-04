# p149 음료수 얼려 먹기

n, m = map(int, input().split())
frame = [0 for _ in range(n)]
for i in range(n):
    frame[i] = list(map(int, input()))
visited = [[False]*m for _ in range(n)]
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(frame, x, y, visited):
    if x < 0 or x > (n-1) or y < 0 or y > (m-1):
        return
    visited[x][y] = True
    for i in range(4):
        if x+dx[i] > (n-1) or y+dy[i] > (m-1):
            continue
        if frame[x+dx[i]][y+dy[i]] == 0 and not visited[x+dx[i]][y+dy[i]]:
            dfs(frame, x+dx[i], y+dy[i], visited)


for j in range(n):
    for k in range(m):
        if frame[j][k] == 0 and not visited[j][k]:
            dfs(frame, j, k, visited)
            count += 1
print(count)