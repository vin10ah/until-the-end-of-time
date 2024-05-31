def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        str_n = str(num)
        for i in str_n:
            if int(i) == k:
                answer += 1

    return answer