def solution(my_string, num1, num2):
    big = max(num1, num2)
    small = min(num1, num2)
    return my_string[:small] + my_string[big] + my_string[small+1:big] + my_string[small] + my_string[big+1:]