def solution(absolutes, signs):
    answer = 0
    for ab, sign in list(zip(absolutes, signs)):
        if sign == True:
            answer += ab
        else:
            answer -= ab
         
    return answer