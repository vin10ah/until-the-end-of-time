def solution(arr, flag):
    answer = []
    for num, fl in list(zip(arr, flag)):
        if fl == True:
            answer += [num for i in range(num*2)]
        else:
            answer = answer[:-num]
    return answer