# p115 왕실의 나이트

knight = input()
row = int(knight[1:])
column = int(ord(knight[:1]) - 96)
count = 0
steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
for step in steps:
    next_row = row + step[0]
    next_col = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count += 1
print(count)