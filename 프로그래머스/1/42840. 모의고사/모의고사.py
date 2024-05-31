''' 
1 = 12345 반복
2 = 21232425 반복
3 = 3311224455 반복
'''
def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score_list = [0,0,0]
    
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            score_list[0] += 1
        if answers[i] == s2[i % len(s2)]:
            score_list[1] += 1
        if answers[i] == s3[i % len(s3)]:
            score_list[2] += 1

    for i in range(len(score_list)):
        if max(score_list) == score_list[i]:
            answer.append(i+1)
    
    return answer
            
            
            
            