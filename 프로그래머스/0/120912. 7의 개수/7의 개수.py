def solution(array):
    str_lst = ''.join([str(num) for num in array])
    answer = [1 for n in str_lst if n == '7']
    
    return sum(answer)