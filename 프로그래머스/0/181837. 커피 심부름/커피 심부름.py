def solution(order):
    answer = 0
    for menu in order:
        if 'americano' in menu or menu == 'anything':
            answer += 4500
        else:
            answer += 5000
            
    return answer