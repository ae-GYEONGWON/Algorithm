import sys

input = sys.stdin.readline

# 확인할 수열의 길이
n = int(input().rstrip())
# 확인할 수열
arr1 = list(map(int, input().split()))
# 확인할 숫자의 수열의 길이
m = int(input().rstrip())
# 확인할 숫자의 수열
arr2 = list(map(int, input().split()))

arr1.sort()
for num in arr2:
    start = 0
    end = n - 1
    # 이분탐색
    while True:
        mid = (start + end)//2
        if arr1[mid] >= num:
            end = mid
        else :
            start = mid + 1
        
        if start == end:
            if  arr1[start] == num:
                print(1)
                break
            else :
                print(0)
                break