# p197 부품 찾기

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
parts_n = list(map(int, input().split()))
m = int(input())
parts_m = list(map(int, input().split()))
parts_n.sort()
for i in range(m):
    if binary_search(parts_n, parts_m[i], 0, n - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')