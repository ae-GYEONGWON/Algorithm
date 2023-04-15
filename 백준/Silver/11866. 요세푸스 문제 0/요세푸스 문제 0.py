# import sys
# from collections import deque
# input = sys.stdin.readline

# n, k = map(int, input().split())
# q = deque([i for i in range(1, n+1)])
# ans = ""
# ptr = 0
# while q:
#     l = len(q)
#     if ptr + 2 >= l:
#         # 원소가 2개 이상일 때
#         if ptr+2-l < l:
#             ptr = ptr+2 - l

#         # 원소가 2개 남았을 때
#         else:
#             ptr = 0
#     else:
#         ptr += 2
#     ans += str(q.pop(ptr)) + " " + ","

# ans = "<" + ans[:-1] + ">"
# print(ans)





import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
res = ""

while q:
    if len(q) > k-1:
        for _ in range(k-1):
            temp = q.popleft()
            q.append(temp)
        res += str(q.popleft()) + "," + " "
    else:
        for _ in range(k-1):
            temp = q.popleft()
            q.append(temp)
        res += str(q.popleft()) + "," + " "

res = "<" + res[:-2] + ">"
print(res)