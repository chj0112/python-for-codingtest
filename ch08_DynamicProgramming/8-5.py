# p226 효율적인 화폐 구성

n, m = map(int, input().split())
value = [int(input()) for _ in range(n)]
value.sort()
d = [10001] * (m + 1)
for i in range(1, m + 1):
    if i in value:
        d[i] = 1
    else:
        for j in value:
            if i - j > 0:
                if d[i - j] != -1:
                    d[i] = min(d[i], d[i - j] + 1)
        if d[i] == 10001:
            d[i] = -1
print(d[m])