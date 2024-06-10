def solution(numbers):
    n_list = list(map(str, numbers))
    n_list.sort(key = lambda x: x*3, reverse = True)
    return str(int(''.join(n_list)))
