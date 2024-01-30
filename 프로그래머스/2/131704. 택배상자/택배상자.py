# from collections import deque

# def solution(order):
#     answer = 1
    
#     # start = order[0]
#     # start보다 작은 자연수를 가진 리스트를 만든다.(보조 컨베이어벨트 = [1,2,3])
#     # start보다 크고 order 길이보다 작은 자연수를 가진 리스트(메인 컨베이어벨트 = [5])
#     # answer += 1
#     # 보조 컨베이어벨트(stack)에서 -1번째 값과 메인의 0번째 값중 order[1]과 일치하는 값을 
#     # 가져온다.
#     # 근데 일치하는 값이 없으면 order에서 보조 컨베이어벨트로 이동시킨뒤에 가져올 수도 있음.
#     # 그러니까 일치시켜야 하는 값이 메인 컨베이어벨트의 0번째 보다 큰 값이면 메인에서 보조로 이동시키고 트럭으로 이송.
#     # 위 과정을 반복하고 불가능 할 경우 함수 종료
#     start = order[0]
#     bojo = [i for i in range(1, start)]
#     main = start+1
    
#     check_num = 1
#     while bojo or main <= len(order):
#         now_order = order[check_num]
#         if now_order == bojo[-1]:
#             bojo.pop()
#             answer += 1
#             check_num += 1
#         elif now_order == main:
#             main += 1
#             answer += 1
#             check_num += 1
#         else:
#             if now_order > main:
#                 bojo.append([i for i in range(main, now_order)])
#                 main = now_order+1
#                 answer += 1
#                 check_num += 1
#             else:
#                 break
        
#     return answer


def solution(order):

    stack = []
    length = len(order)
    index = 0
    for num in range(1, length + 1):
        stack.append(num)

        while stack and stack[-1] == order[index]:
            stack.pop()
            index += 1


    return index