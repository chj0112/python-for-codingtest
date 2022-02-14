# p217 1로 만들기

x = int(input())
d = [30000] * 30001
d[1] = 0

for i in range(2, x + 1):
    if i % 5 == 0:
        d[i] = min(d[i // 5] + 1, d[i])
    if i % 3 == 0:
        d[i] = min(d[i // 3] + 1, d[i])
    if i % 2 == 0:
        d[i] = min(d[i // 2] + 1, d[i])
    d[i] = min(d[i - 1] + 1, d[i])

print(d[x])