def solution(s):
    answer = []
    for i in s:
        answer.append(i)
    answer.sort(reverse=True)
    return ''.join(answer)