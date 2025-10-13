import sys

input = sys.stdin.readline

n = int(input())
x_list = list(map(int, input().split()))

sorted_x_list = sorted(list(set(x_list)))

for x in x_list:
    start = 0
    end = len(sorted_x_list)
    while start <= end:
        mid = (start + end)//2
        
        if sorted_x_list[mid] == x:
            print(mid, end=" ")
            break
        
        if sorted_x_list[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
            