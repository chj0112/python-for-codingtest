# p312 곱하기 혹은 더하기

s = input()
n = int(s[0])
for i in range(1, len(s)):
    if n == 0 or n == 1 or s[i] == '0' or s[i] == '1':
        n += int(s[i])
    else:
        n *= int(s[i])
print(n)