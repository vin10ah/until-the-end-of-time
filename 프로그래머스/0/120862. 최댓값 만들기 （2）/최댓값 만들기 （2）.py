def solution(numbers):
    numbers.sort()
    minn = numbers[0] * numbers[1]
    maxn = numbers[-2] * numbers[-1]
    return max(minn, maxn)