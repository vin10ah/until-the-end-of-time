def solution(x):
    nsum = 0
    xlst = [int(n) for n in str(x)]
    return True if x % sum(xlst)==0 else False