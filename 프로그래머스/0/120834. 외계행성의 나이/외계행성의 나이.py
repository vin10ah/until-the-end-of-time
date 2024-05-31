# def solution(age):
#     alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#     age = str(age)
#     new_age = ''
#     for num in age:
#         new_age += alpha[int(num)]
        
#     return str(new_age)

def solution(age):
    
    table = str.maketrans('0123456789', 'abcdefghij')
      
    return str(age).translate(table)
