def solution(n, words):
    answer = []
    word_list = []
    
    def make_ans(word_list, n, answer):
        temp = (len(word_list)+1)%n
        answer.append(temp if temp != 0 else n)
        answer.append(len(word_list)//n+1)
        return answer;
    
    word_list.append(words[0])
    for word in words[1:]:
        if word in word_list:
            answer = make_ans(word_list, n, answer)
            break
        else:
            if word[0] == word_list[-1][-1]:
                word_list.append(word)
            else:
                answer = make_ans(word_list, n, answer)
                break
    else:
        return [0, 0]    
    

    return answer