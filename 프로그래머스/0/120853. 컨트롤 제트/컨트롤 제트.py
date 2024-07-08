def solution(s):
    answer = []
    s_list = s.split()
    for e in s_list:
        if e == 'Z':
            answer.pop()
        else:
            answer.append(int(e))
    return sum(answer)