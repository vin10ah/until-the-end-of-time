def solution(s):
    answer = []
    s_list = s.split(' ')
    for i in s_list:
        if i:
            new_s = i[0].upper() + i[1:].lower()
            answer.append(new_s)
        else:
            answer.append('')
    return ' '.join(answer)

