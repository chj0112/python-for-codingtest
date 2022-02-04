# p110 상하좌우

n = int(input())
route = list(input().split())
x = 1
y = 1
for i in range(len(route)):
    if (route[i] == 'L'):
        if (1 < y <= n):
            y -= 1
    elif (route[i] == 'R'):
        if (1 <= y < n):
            y += 1
    elif (route[i] == 'U'):
        if (1 < x <= n):
            x -= 1
    elif (route[i] == 'D'):
        if (1 <= x < n):
            x += 1
print(x, y)