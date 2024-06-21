def solution(num):
    nnum = num
    cnt = 0
    while nnum > 0:
        if nnum == 1:
            if cnt <= 500:
                return cnt
            else:
                return -1
        if nnum % 2 == 0:
            nnum = nnum / 2
        else:
            nnum = nnum * 3 + 1
        cnt += 1
