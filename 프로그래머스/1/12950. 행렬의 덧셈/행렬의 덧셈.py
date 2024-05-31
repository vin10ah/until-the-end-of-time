def solution(arr1, arr2):
    answer = []

    for A, B in zip(arr1, arr2):
        l = []
        for a, b in zip(A, B):
            l.append(a+b)
        answer.append(l)
            
    return answer

# def solution(arr1, arr2):
#     for i in range(len(arr1))