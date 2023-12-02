def solution(n, m):
    answer = []
    answer.append(GCD(n, m))
    answer.append(LCM(n, m))
    
    return answer

def GCD(num1, num2):
    result1 = set()
    result2 = set()
    for i in range(1, int(num1**0.5)+1):
        if num1 % i == 0:
            result1.add(num1//i)
            result1.add(i)
            
    for i in range(1, int(num2**0.5)+1):
        if num2 % i == 0:
            result2.add(num2//i)
            result2.add(i)
    return max(list(result1 & result2));
    
def LCM(num1, num2):
    for i in range(max(num1, num2), 1000001):
        if i % num1 == 0 and i % num2 == 0:
            return i;