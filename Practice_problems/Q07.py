# p321 럭키 스트레이트

n = input()
half = int(len(n) / 2)
a = n[:half]
b = n[half:]
sum_a, sum_b = 0, 0
for i in a:
    sum_a += int(i)
for i in b:
    sum_b += int(i)
if sum_a == sum_b:
    print("LUCKY")
else:
    print("READY")