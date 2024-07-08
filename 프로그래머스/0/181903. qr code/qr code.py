def solution(q, r, code):
    answer = [code[i] for i in range(len(code)) if i % q == r ]
    return ''.join(answer)