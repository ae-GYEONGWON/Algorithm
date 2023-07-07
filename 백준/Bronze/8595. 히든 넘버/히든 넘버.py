import sys, re
input = sys.stdin.readline

n = int(input())
string = input().rstrip()

numbers = re.findall(r'\d+', string)
result = 0
for i in numbers:
    result += int(i)

print(result)