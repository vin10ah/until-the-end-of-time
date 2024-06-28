def solution(num_list):
    cnt = 0
    for num in num_list:
        while num > 0:
            if num == 1:
                break
            else:
                if num % 2 == 0:
                    num /= 2
                else:
                    num = (num-1)/2
            cnt += 1
    
    return cnt