import sys
input = sys.stdin.readline

S = input().rstrip()
i = 0;
while i < len(S):
    start = 0

    if S[i] == " ":
        print(" ", end="")
        i += 1
    elif S[i] == "<":
        start = i
        while i+1 < len(S) and S[i] != ">":
            i += 1;
        
        for j in range(start, i+1):
            print(S[j], end="")
        i += 1
    else:
        start = i
        while i < len(S) and S[i] != " " and S[i] != "<":
            i += 1
        
        for j in range(i-1, start-1, -1):
            print(S[j], end="")
        