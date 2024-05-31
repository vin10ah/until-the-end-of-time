def solution(before, after):#
    b_list = sorted(list(before))
    a_list = sorted(list(after))

    return 1 if b_list == a_list else 0