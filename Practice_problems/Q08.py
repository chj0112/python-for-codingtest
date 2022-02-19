# p322 문자열 재정렬

s = input()
n = 0
data = []

for i in s:
    if 48 <= ord(i) <= 57:  # isdigit 함수 사용하는 것이 더 간편
        n += int(i)
    else:
        data.append(i)

data.sort()

for i in data:
    print(i, end='')
print(n)