def solution(myString, pat):
    pidx = myString.rindex(pat[-1])
    
    return myString[:pidx+1]