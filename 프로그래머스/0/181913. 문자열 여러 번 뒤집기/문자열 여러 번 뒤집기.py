def solution(my_string, queries):
    my_string = list(my_string) 
    
    for s, e in queries:
        new_str = my_string[s:e+1][::-1]
        my_string[s:e+1] = new_str
        
    return ''.join(my_string)