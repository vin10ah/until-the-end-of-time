def solution(arr, divisor):
    answer = sorted([num for num in arr if num % divisor == 0])
    if len(answer) == 0:
        answer.append(-1) 
        return answer
    else:
        return answer