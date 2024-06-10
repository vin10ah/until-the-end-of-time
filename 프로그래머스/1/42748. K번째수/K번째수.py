def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c[0]-1, c[1], c[2]-1
        new = sorted(array[i:j])
        answer.append(new[k])
    return answer
