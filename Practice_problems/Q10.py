# p325 자물쇠와 열쇠

def turnright(n, lock):
    rt_lock = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            rt_lock[y][n - x - 1] = lock[x][y]
    return rt_lock


def unlock(n, m, key, lock):
    new_lock = [[0] * (n + 2 * m - 2) for _ in range(n + 2 * m - 2)]
    for x in range(n):
        for y in range(n):
            new_lock[x + m - 1][y + m - 1] = lock[x][y]
    for i in range(len(new_lock) - (m - 1)):
        for j in range(len(new_lock) - (m - 1)):
            count = 0
            temp = [[0] * (n + 2 * m - 2) for _ in range(n + 2 * m - 2)]
            for x in range(n + 2 * m - 2):
                for y in range(n + 2 * m - 2):
                    temp[x][y] = new_lock[x][y]
            for x in range(m):
                for y in range(m):
                    temp[i + x][j + y] += key[x][y]
            for k in range(m - 1, m - 1 + n):
                for l in range(m - 1, m - 1 + n):
                    if temp[k][l] != 1:
                        count += 1
            if count == 0:
                return True
    return False


def solution(key, lock):
    answer = False
    for i in range(4):
        answer = unlock(len(lock), len(key), key, lock)
        if answer:
            return answer
        else:
            lock = turnright(len(lock), lock)
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))