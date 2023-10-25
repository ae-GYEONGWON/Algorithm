def check (x):
    if -5 <= x <= 5:
        return True;
    return False;

def solution(dirs):
    dp = {"U": [], "D": [], "R": [], "L": []}
    now = [0, 0]
    answer = 0

    for i, dir in enumerate(dirs):
        if dir == "U":
            if now not in dp["U"]:
                if check(now[1]+1):
                    dp["U"].append(now.copy())  # now 리스트의 복사본을 저장
                    now[1] += 1
                    dp["D"].append(now.copy())
                    answer += 1
            else:
                if check(now[1]+1):
                    now[1] += 1

        elif dir == "D":
            if now not in dp["D"]:
                if check(now[1]-1):
                    dp["D"].append(now.copy())
                    now[1] -= 1
                    dp["U"].append(now.copy())
                    answer += 1
            else:
                if check(now[1]-1):
                    now[1] -= 1
                    
        elif dir == "R":
            if now not in dp["R"]:
                if check(now[0]+1):
                    dp["R"].append(now.copy())
                    now[0] += 1
                    dp["L"].append(now.copy())
                    answer += 1
            else:
                if check(now[0]+1):
                    now[0] += 1

        elif dir == "L":
            if now not in dp["L"]:
                if check(now[0]-1):
                    dp["L"].append(now.copy())
                    now[0] -= 1
                    dp["R"].append(now.copy())
                    answer += 1
            else:
                if check(now[0]-1):
                    now[0] -= 1

    return answer
