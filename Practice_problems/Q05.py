# p315 볼링공 고르기

n, m = map(int, input().split())
weight = list(map(int, input().split()))
count = 0
for i in weight:
    for j in weight:
        if j > i:
            count += 1
print(count)


# 더 효율적인 코드
# n, m = map(int, input().split())
# weight = list(map(int, input().split()))
# array = [0] * (m + 1)
# for x in weight:
#     array[x] += 1
# count = 0
# for i in range(1, m + 1):
#     n -= array[i]
#     count += array[i] * n
# print(count)