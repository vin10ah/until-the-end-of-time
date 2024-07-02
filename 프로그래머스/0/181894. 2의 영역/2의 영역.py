def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(arr.index(arr[i],i))
    
    return [-1] if len(answer) == 0 else arr[answer[0]:answer[-1]+1]