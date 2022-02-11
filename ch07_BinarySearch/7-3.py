# p201 떡볶이 떡 만들기

n, m = map(int, input().split())
height = list(map(int, input().split()))
h = max(height)
cut = 0
while cut < m:
    h -= 1
    for i in height:
        if i > h:
            i -= 1
            cut += 1
print(h)


# 이진탐색을 이용한 풀이
# def binary_search(array, target, start, end):
#     result = 0
#     while start <= end:
#         mid = (start + end) // 2
#         cut = 0
#         for i in array:
#             if i > mid:
#                 cut += i - mid
#         if cut == target:
#             return mid
#         elif cut > target:
#             result = mid
#             start = mid + 1
#         else:
#             end = mid - 1
#     return result
#
#
# n, m = map(int, input().split())
# height = list(map(int, input().split()))
# print(binary_search(height, m, 0, max(height)))