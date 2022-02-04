# p87 거스름돈

n = int(input())
coin = [500, 100, 50, 10]
count = 0

for i in coin:
    count += n // i
    n %= i

print(count)