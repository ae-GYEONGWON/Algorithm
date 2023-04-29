from collections import deque

equation = deque(input().split('-'))
answer = 0
# print(equation)
if equation[0] == '':
    equation.popleft()
    for x in equation.popleft().split('+'):
        answer -= int(x)
else :
    for x in equation.popleft().split('+'):
        answer += int(x)
while equation:
    x = equation.popleft().split('+')
    for y in x:
        answer -= int(y)
print(answer)