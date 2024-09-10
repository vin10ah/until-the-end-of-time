def solution(food):
    answer = ''
    batch = ''
    for i in range(len(food)):
        answer += str(i) * (food[i] // 2)
    r_answer = ''.join(sorted(answer, reverse=True))
    return answer + '0' + r_answer