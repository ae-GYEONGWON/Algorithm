def solution(record):
    answer = []
    
    user_dic = {}
    command_list = []
    
    for r in record:
        r = r.split(" ")
        if r[0] == "Leave":
            command, uid = r
            
            command_list.append(command + " " + uid)
        else:
            command, uid, name = r
            
            user_dic[uid] = name
            if command != "Change":
                command_list.append(command + " " + uid)
            
    for command in command_list:
        command, uid = command.split(" ")
        
        if command == "Enter":
            answer.append(f"{user_dic[uid]}님이 들어왔습니다.")
        else:
            answer.append(f"{user_dic[uid]}님이 나갔습니다.")
    
    return answer