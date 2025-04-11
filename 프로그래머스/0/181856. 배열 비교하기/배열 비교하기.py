def solution(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    
    if l1 > l2:
        return 1
    if l1 < l2:
        return -1
    if sum(arr1) > sum(arr2):
        return 1
    elif sum(arr2) > sum(arr1):
        return -1
    return 0