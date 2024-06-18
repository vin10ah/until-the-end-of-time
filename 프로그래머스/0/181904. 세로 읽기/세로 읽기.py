def solution(my_string, m, c):
    answer = ''
    sen = ''
    
    for s in my_string:
        if len(sen) == m:
            answer += sen[c-1]
            sen = ''
        sen += s
    answer += sen[c-1]
    
    
    return answer