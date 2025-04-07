def solution(arr, n):
    if len(arr) % 2 == 0:
        for idx in range(1, len(arr), 2):
            arr[idx] += n
    else:
        for idx in range(0, len(arr), 2):
            arr[idx] += n
    return arr