# p303 커리큘럼

# 위상 정렬 알고리즘 사용
from collections import deque

n = int(input())
indegree = [0] * (n + 1)
time = [0] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    l = deque(map(int, input().split()))
    time[i] = l.popleft()
    while l:
        e = l.popleft()
        if e == -1:
            break
        indegree[i] += 1
        graph[e].append(i)


def topology_sort():
    result = [0] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result[now] += time[now]
        for i in graph[now]:
            result[i] = max(result[now], result[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])


topology_sort()