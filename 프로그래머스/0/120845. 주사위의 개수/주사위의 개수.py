def solution(box, n):
    n_box = [size // n for size in box]
    cnt = 1
    for i in n_box:
        cnt *= i
    return cnt