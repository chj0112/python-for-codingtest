# p118 게임 개발

n, m = map(int, input().split())
a, b, d = map(int, input().split())
count = 1
arr = [0 for k in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
arr[a][b] = 2
while(True):
    if (arr[a - 1][b] == 1 or arr[a - 1][b] == 2) and (arr[a + 1][b] == 1 or arr[a + 1][b] == 2) and (arr[a][b - 1] == 1 or arr[a][b - 1] == 2) and (arr[a][b + 1] == 1 or arr[a][b + 1] == 2):
        if d == 0:
            if arr[a + 1][b] == 1:
                break
            else:
                a += 1
        if d == 1:
            if arr[a][b - 1] == 1:
                break
            else:
                b -= 1
        if d == 2:
            if arr[a - 1][b] == 1:
                break
            else:
                a -= 1
        if d == 3:
            if arr[a][b + 1] == 1:
                break
            else:
                b += 1
    elif d == 0:
        if arr[a][b - 1] == 0:
            d = 3
            b -= 1
            arr[a][b] = 2
            count += 1
        else:
            d = 3
    elif d == 1:
        if arr[a - 1][b] == 0:
            d = 0
            a -= 1
            arr[a][b] = 2
            count += 1
        else:
            d = 0
    elif d == 2:
        if arr[a][b + 1] == 0:
            d = 1
            b += 1
            arr[a][b] = 2
            count += 1
        else:
            d = 1
    elif d == 3:
        if arr[a + 1][b] == 0:
            d = 2
            a += 1
            arr[a][b] = 2
            count += 1
        else:
            d = 2
print(count)