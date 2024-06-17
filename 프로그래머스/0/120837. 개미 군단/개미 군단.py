def solution(hp):
    a = [5, 3, 1]
    cnt = 0
    i = 0
    while hp > 0:
        b = divmod(hp, a[i])
        cnt += b[0]
        hp = b[1]
        i += 1
        
    return cnt+hp
