# p220 개미 전사

n = int(input())
k = list(map(int, input().split()))

d = [0] * 101   # 해당 자리까지의 최댓값을 저장하기 위한 DP 테이블 초기화

# Bottom-UP 방식 Dynamic Programming 진행
d[1] = k[0]
for i in range(2, n + 1):
    d[i] = max(d[i - 2] + k[i - 1], d[i - 1])
print(d[n])