def solution(n):
    answer = 0
    x = n ** 0.5 
    
    if x.is_integer():
        return (x+1)**2
    else:
        return -1