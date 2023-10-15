from collections import defaultdict

def solution(str1, str2):
    
    dic_str1 = defaultdict(int)
    for i, v in enumerate(str1[:-1]):
        temp = str1[i]+str1[i+1]
        if temp.isalpha():
            dic_str1[temp.lower()] += 1
        
    dic_str2 = defaultdict(int)
    for i, v in enumerate(str2[:-1]):
        temp = str2[i]+str2[i+1]
        if temp.isalpha():
            dic_str2[temp.lower()] += 1
        
    # 교집합, 합집합 수 구하기
    str1Nstr2 = 0; str1Ustr2 = 0
    for key in dic_str1.keys():
        if key in dic_str2:
            str1Nstr2 += min(dic_str1[key], dic_str2[key])
            str1Ustr2 += max(dic_str1[key], dic_str2[key])
        else:
            str1Ustr2 += dic_str1[key]
    for key in dic_str2.keys():
        if key not in dic_str1:
            str1Ustr2 += dic_str2[key]

    if str1Ustr2 == 0:
        return 65536;
    return int((str1Nstr2/str1Ustr2)*65536)
