# p314 만들 수 없는 금액

n = int(input())
coin = list(map(int, input().split()))
arr = []
money = 1
for i in coin:
    for j in range(len(arr)):
        arr.append(i + arr[j])
    arr.append(i)
    arr = list(set(arr))
while True:
    if money not in arr:
        print(money)
        break
    else:
        money += 1


# 좀 더 간단한 구현
# n = int(input())
# coin = list(map(int, input().split()))
# coin.sort()
# money = 1
# for x in coin:
#     if money < x:
#         break
#     money += x
# print(money)