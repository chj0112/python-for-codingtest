# p311 모험가 길드

n = int(input())
x = list(map(int, input().split()))
x.sort()
count = 0
while x:
    if x[-1] > len(x):
        break
    l = []
    while True:
        temp = x.pop(0)
        l.append(temp)
        if len(l) == temp:
            break
    count += 1
print(count)