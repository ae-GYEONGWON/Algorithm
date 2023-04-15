t = int(input())
PSs = [input() for _ in range(t)]

for PS in PSs:
    stack = [""]*50
    ptr = 0
    size = 0
    for i in PS:
        if i == "(":
            stack[ptr] = i
            ptr += 1
            size += 1
        elif i == ")":
            if stack[ptr-1] =="(":
                ptr -= 1
                stack[ptr] = ""
                size -= 1
            else:
                print("NO")
                break
    else:
        if size == 0:
            print("YES")
        else:
            print("NO")