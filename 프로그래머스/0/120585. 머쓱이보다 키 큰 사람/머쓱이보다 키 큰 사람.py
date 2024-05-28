def solution(array, height):
    count = 0
    for f_height in array:
        if f_height > height:
            count += 1
    return count