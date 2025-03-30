def solution(my_string):
    answer=""
    for s in my_string:
        answer+=s.lower()
    return "".join(sorted(list(answer)))