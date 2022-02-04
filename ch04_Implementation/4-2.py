# p113 시각

n = int(input())
count = 0

for h in range(n + 1):
    h10 = h // 10
    h1 = h % 10

    for m in range(60):
        m10 = m // 10
        m1 = m % 10

        for s in range(60):
            s10 = s // 10
            s1 = s % 10
            if h10 == 3 or h1 == 3 or m10 == 3 or m1 == 3 or s10 == 3 or s1 == 3:
                count += 1

print(count)