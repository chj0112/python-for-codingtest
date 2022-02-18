# p316 무지의 먹방 라이브

def solution(food_times, k):
    answer = 0
    for i in range(k):
        food_times[answer] -= 1
        answer = (answer + 1) % len(food_times)
        for j in range(len(food_times)):
            if food_times[answer] != 0:
                break
            answer = (answer + 1) % len(food_times)
        if food_times.count(0) == len(food_times):
            answer = -2
            break
    answer += 1
    return answer


print(solution([3, 1, 2], 5))