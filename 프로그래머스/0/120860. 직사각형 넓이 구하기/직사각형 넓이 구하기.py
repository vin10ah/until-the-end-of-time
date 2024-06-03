def solution(dots):
    dot_x = []
    dot_y = []
    for x, y in dots:
        dot_x.append(x)
        dot_y.append(y)
    x_len = max(dot_x)-min(dot_x)
    y_len = max(dot_y)-min(dot_y)
        
    return x_len * y_len
