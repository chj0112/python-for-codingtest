# p327 뱀

n = int(input())
k = int(input())
apple = []

for i in range(k):
    apple.append(list(map(int, input().split())))

l = int(input())
data = []

for i in range(l):
    data.append(list(input().split()))
    data[i][0] = int(data[i][0])

# 0: 빈 공간, 1: 뱀, 2: 사과
board = [[0] * (n + 1) for _ in range(n + 1)]
board[1][1] = 1

for i in apple:
    board[i[0]][i[1]] = 2

# 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀은 처음에 오른쪽을 향함
direction = 0

# snake 배열에 뱀이 지나간 좌표를 큐 개념으로 구현
snake = [[1, 1]]
time = 0


def go(board, snake, n, d, x):
    current = (1, 1)
    while True:
        x += 1
        new_x = current[0] + dx[d]
        new_y = current[1] + dy[d]
        # 행 길이 초과, 열 길이 초과, 자기 자신의 몸과 부딪힐 때의 시간값 반환
        if not 0 < new_x <= n or not 0 < new_y <= n or board[new_x][new_y] == 1:
            return x
        # 사과가 있는 칸에서 뱀의 꼬리는 움직이지 않음
        if board[new_x][new_y] == 2:
            board[new_x][new_y] = 1
            snake.append([new_x, new_y])
        # 사과가 없는 칸에서 뱀의 꼬리가 위치한 칸을 비워줌
        else:
            board[new_x][new_y] = 1
            snake.append([new_x, new_y])
            remove = snake.pop(0)
            board[remove[0]][remove[1]] = 0
        current = (new_x, new_y)
        if len(data) != 0:
            if x == data[0][0]:
                d = turn(data.pop(0)[1], d)


def turn(c, d):
    if c == 'L':
        d -= 1
        if d == -1:
            d = 3
    elif c == 'D':
        d += 1
        if d == 4:
            d = 0
    return d


print(go(board, snake, n, direction, time))