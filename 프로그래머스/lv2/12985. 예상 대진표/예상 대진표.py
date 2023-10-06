def change_num(n):
    if n % 2 == 0:
        return n//2
    else:
        return (n+1)//2

def solution(n,a,b):
    answer = 0

    # 1,2 => 1
    # 3,4 => 2
    # 5,6 => 3
    # 7,8 => 4
    # 9, 10 => 5
    # 8 => 4 => 2
    # n을 2로 나누고 answer += 1
    # a, b를 조정 => 짝수로 바꾸고 나누기 2
    # 만약 abs(a-b) = 1 and a+b+1의 제곱근이 2의 배수인지
    # 2의 배수면 둘이 한팀이니까 리턴
    while n != 1:
        if a == b:
            return answer
        n //= 2
        a = change_num(a)
        b = change_num(b)
        answer+=1
            

    return answer