def solution(emergency):
    re_emer = sorted(emergency, reverse=True)
    emer = [re_emer.index(i)+1 for i in emergency]
    return emer