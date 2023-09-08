def solution(elements):
    answer = set()
    
    new_elements = elements + elements[:-1]
    for n in range(1, len(elements)):
        for i, ele in enumerate(new_elements[:len(elements)]):
            answer.add(sum(new_elements[i:i+n]))
    answer.add(sum(elements))
    # print(answer)
    return len(answer)