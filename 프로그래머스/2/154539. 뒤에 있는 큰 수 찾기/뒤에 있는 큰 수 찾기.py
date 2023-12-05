# def solution(numbers):
#     answer = []
    
#     for idx, number in enumerate(numbers):
#         for next_idx in range(idx+1, len(numbers)):
#             if number < numbers[next_idx]:
#                 answer.append(numbers[next_idx])
#                 break

#         else:
#             answer.append(-1)
        
    
#     return answer

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number

        stack.append(idx)

    return answer
