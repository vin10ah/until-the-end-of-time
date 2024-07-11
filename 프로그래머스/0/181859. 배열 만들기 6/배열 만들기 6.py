def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
        elif len(stk) > 0 and stk[-1] == arr[i]:
            stk.pop()
        elif len(stk) > 0 and stk[-1] != arr[i]:
            stk.append(arr[i])
        i += 1
    
    return stk if stk else [-1]