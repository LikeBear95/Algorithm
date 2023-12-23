def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[-1])
        for num in range(0, len(numbers) - 1):
            answer.append(numbers[num])
    elif direction == "left":
        for num in range(1, len(numbers)):
            answer.append(numbers[num])
        answer.append(numbers[0])
    return answer