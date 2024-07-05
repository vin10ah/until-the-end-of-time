def solution(price, money, count):
    total = sum([price * i for i in range(1, count+1)])
    
    return abs(money - total) if money - total < 0 else 0