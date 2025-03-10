def solution(myString, pat):
    return int(pat in "".join(["B" if s=="A" else "A" for s in myString]))