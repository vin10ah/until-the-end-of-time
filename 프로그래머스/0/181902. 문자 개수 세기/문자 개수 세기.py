def solution(my_string):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    answer = [0] * 52 
    for s in my_string:
        if s.islower():
            answer[alp.index(s)+26] += 1
        else:
            answer[alp.index(s.lower())] += 1
    return answer