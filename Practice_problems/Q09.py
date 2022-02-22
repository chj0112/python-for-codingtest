# p323 문자열 압축

def solution(s):
    answer = 0
    str = list(s)
    min_cnt = len(str)
    for i in range(1, len(str) // 2 + 1):
        l = []
        cnt = 0
        temp = 0
        for j in range(len(str) // i):
            l.append(str[i * j:i * j + i])
            if j == 0:
                cnt += i
            elif l[j - 1] == l[j]:
                temp += 1
                if temp == 1:
                    cnt += 1
            else:
                temp = 0
                cnt += i
        cnt += len(str) % i
        min_cnt = min(min_cnt, cnt)
    answer = min_cnt
    return answer


print(solution("aabbaccc"))