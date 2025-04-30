def solution(todo_list, finished):
    return [todo_list[i] for i, e in enumerate(finished) if e == False]