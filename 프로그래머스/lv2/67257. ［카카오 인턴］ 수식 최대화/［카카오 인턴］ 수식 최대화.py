from itertools import permutations
from copy import deepcopy

def operation(num1, num2, op):
    if op == "+":
        return str(int(num1) + int(num2))
    elif op == "-":
        return str(int(num1) - int(num2))
    else:
        return str(int(num1) * int(num2))
    
def calculation(exp, op):
    array = deepcopy(exp)

    for o in op:
        stack = []
        while array:
            temp = array.pop(0)
            if temp == o:
                stack.append(operation(stack.pop(), array.pop(0), temp))
            else:
                stack.append(temp)
        array = stack
    return abs(int(stack[0]))

def solution(expression):
    answer = 0
    
    array = []
    temp = ""
    for i in expression:
        if i not in ["-", "+", "*"]:
            temp += i
        else:
            array.append(temp)
            temp = ""
            array.append(i)
    array.append(temp)
    
    op = list(permutations(["-", "+", "*"], 3))
    for o in op:
        temp = calculation(array, o)
        if answer < temp:
            answer = temp
    
    
    return answer