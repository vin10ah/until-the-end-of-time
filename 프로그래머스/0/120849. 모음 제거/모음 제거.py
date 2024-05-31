def solution(my_string):
    table = str.maketrans('aeiou','.....')
    return my_string.translate(table).replace('.', '')