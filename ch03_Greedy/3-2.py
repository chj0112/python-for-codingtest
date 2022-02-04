# p92 큰 수의 법칙

n, m, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
a = l[n-1]
b = l[n-2]
result = 0
for i in range(m):
    if(i % (k+1) == k):
        result += b
    else:
        result += a
print(result)