# p329 기둥과 보 설치

# 답안 코드 참조할 것
# 아래 코드처럼 풀지 말자
def solution(n, build_frame):
    answer = []
    pillar = [[0] * (n + 1) for _ in range(n + 1)]
    beam = [[0] * (n + 1) for _ in range(n + 1)]
    for i in build_frame:
        if i[3] == 0:
            if [i[0], i[1], i[2]] in answer:
                if i[2] == 0:
                    if i[0] == 0:
                        if (pillar[i[0]][i[1] + 1] == 1 and beam[i[0]][i[1] + 1] == 0) or (beam[i[0]][i[1] + 1] == 1 and pillar[i[0] + 1][i[1]] == 0):
                            continue
                    elif i[0] == n:
                        if (pillar[i[0]][i[1] + 1] == 1 and beam[i[0] - 1][i[1] + 1] == 0) or (beam[i[0] - 1][i[1] + 1] == 1 and pillar[i[0] - 1][i[1]] == 0):
                            continue
                    elif (pillar[i[0]][i[1] + 1] == 1 and beam[i[0] - 1][i[1] + 1] == 0 and beam[i[0]][i[1] + 1] == 0) or (beam[i[0] - 1][i[1] + 1] == 1 and pillar[i[0] - 1][i[1]] == 0 and beam[i[0]][i[1] + 1] == 0) or (beam[i[0]][i[1] + 1] == 1 and pillar[i[0] + 1][i[1]] == 0 and beam[i[0] - 1][i[1] + 1] == 0):
                        continue
                    pillar[i[0]][i[1]] = 0
                    answer.remove([i[0], i[1], i[2]])
                elif i[2] == 1:
                    if i[0] == 0:
                        if (beam[i[0] + 1][i[1]] == 1 and pillar[i[0] + 1][i[1] - 1] == 0 and pillar[i[0] + 2][i[1] - 1] == 0) or (pillar[i[0]][i[1]] == 1 and pillar[i[0]][i[1] - 1] == 0):
                            continue
                    elif i[0] == n - 1:
                        if (beam[i[0] - 1][i[1]] == 1 and pillar[i[0] - 1][i[1] - 1] == 0 and pillar[i[0]][i[1] - 1] == 0) or (beam[i[0] + 1][i[1]] == 1 and pillar[i[0] + 1][i[1] - 1] == 0) or (pillar[i[0]][i[1]] == 1 and pillar[i[0]][i[1] - 1] == 0 and beam[i[0] - 1][i[1]] == 0):
                            continue
                    elif (beam[i[0] - 1][i[1]] == 1 and pillar[i[0] - 1][i[1] - 1] == 0 and pillar[i[0]][i[1] - 1] == 0) or (beam[i[0] + 1][i[1]] == 1 and pillar[i[0] + 1][i[1] - 1] == 0 and pillar[i[0] + 2][i[1] - 1] == 0) or (pillar[i[0]][i[1]] == 1 and pillar[i[0]][i[1] - 1] == 0 and beam[i[0] - 1][i[1]] == 0):
                        continue
                    beam[i[0]][i[1]] = 0
                    answer.remove([i[0], i[1], i[2]])
        elif i[3] == 1:
            if i[2] == 0:
                if i[1] == 0 or beam[i[0]][i[1]] == 1 or beam[i[0] - 1][i[1]] == 1 or pillar[i[0]][i[1] - 1] == 1:
                    pillar[i[0]][i[1]] = 1
                    answer.append([i[0], i[1], i[2]])
            elif i[2] == 1:
                if pillar[i[0]][i[1] - 1] == 1 or pillar[i[0] + 1][i[1] - 1] == 1 or (beam[i[0] - 1][i[1]] == 1 and beam[i[0] + 1][i[1]] == 1):
                    beam[i[0]][i[1]] = 1
                    answer.append([i[0], i[1], i[2]])
    answer.sort()
    return answer


print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))