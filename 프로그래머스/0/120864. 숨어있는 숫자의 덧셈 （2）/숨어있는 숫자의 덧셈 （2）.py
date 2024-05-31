def solution(my_string):
    answer = 0
    new_str = ''
    for string in my_string:
        if string.isdigit():
            new_str += string
        else:
            new_str += '.'

    return sum([int(x) for x in new_str.split('.') if x.isdigit()])