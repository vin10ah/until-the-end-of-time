def solution(numlist, n):
    dic = {}
    numlist.sort(reverse=True)
    for num in numlist:
        diff = abs(num - n)
        if diff not in dic:
            dic[diff] = f'{num},'
        else:
            dic[diff] += f'{num},'
            
    num_concat = ''
    for _, nums in sorted(dic.items()):
        num_concat += nums
    answer = num_concat.split(',')
    answer = [int(n) for n in answer if n.isnumeric()]
    return answer