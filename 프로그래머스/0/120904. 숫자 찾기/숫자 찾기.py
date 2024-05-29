def solution(num, k):
    answer = 0
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] == str(k):
            return i+1
        else:
            answer = -1
            
    return answer