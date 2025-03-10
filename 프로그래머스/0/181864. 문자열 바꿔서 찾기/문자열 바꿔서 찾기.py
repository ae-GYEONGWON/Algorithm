def solution(myString, pat):
    if pat in "".join(["B" if s=="A" else "A" for s in myString]):
        return 1
    return 0