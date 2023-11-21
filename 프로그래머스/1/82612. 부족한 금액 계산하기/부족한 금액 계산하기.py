def solution(price, money, count):
    answer = -1    
    
    return max(price*((count*(count+1))//2)-money, 0)