def solution(arr):
    answer = []
    if len(arr) > len(arr[0]):
        diff = [0] * (len(arr) - len(arr[0]))
        for e in arr:
            answer.append(e+diff)
        return answer
    else:
        diff = len(arr[0]) - len(arr)
        add_arr = [0 for i in range(len(arr[0]))]
        for i in range(diff):
            arr.append(add_arr)
        return arr