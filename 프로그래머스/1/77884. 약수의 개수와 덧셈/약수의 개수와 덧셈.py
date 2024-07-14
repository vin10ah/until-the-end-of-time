def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        d_lst = [j for j in range(1, i+1) if i % j == 0]
        if len(d_lst) % 2 == 0:
            answer += d_lst[-1]
        else:
            answer -= d_lst[-1]
    return answer