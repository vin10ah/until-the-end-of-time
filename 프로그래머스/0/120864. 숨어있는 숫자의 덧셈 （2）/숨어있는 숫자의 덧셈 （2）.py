# def solution(my_string):
#     new_str = ''
#     for string in my_string:
#         if string.isdigit():
#             new_str += string
#         else:
#             new_str += ' '

#     return sum([int(x) for x in new_str.split(' ') if x.isdigit()])

def solution(my_string):
    new_str = ''.join(string if string.isdigit() else ' ' for string in my_string)

    return sum([int(x) for x in new_str.split(' ') if x.isdigit()])