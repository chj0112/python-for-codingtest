# p180 성적이 낮은 순서로 학생 출력하기

# 딕셔너리를 이용한 풀이
n = int(input())
students = dict()
for _ in range(n):
    a, b = input().split()
    b = int(b)
    students[a] = b

sorted_students = dict(sorted(students.items(), key=lambda x: x[1]))

for key in sorted_students:
    print(key, end=' ')



# 삽입정렬을 이용한 풀이
# n = int(input())
# student = []
# for i in range(n):
#     student.append(list(input().split()))
#     student[i][1] = int(student[i][1])
#
# def sortST(student, n):
#     for i in range(n):
#         for j in range(i + 1, n):
#             if (student[i][1] > student[j][1]):
#                 min = j
#                 student[i][0], student[min][0] = student[min][0], student[i][0]
#                 student[i][1], student[min][1] = student[min][1], student[i][1]
#     return student
#
# sortST(student, n)
# for i in range(n):
#     print(student[i][0], end=' ')