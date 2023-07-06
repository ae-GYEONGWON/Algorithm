import sys
input = sys.stdin.readline

x = input().rstrip()

if x[:2] == "0x":
    print(int(x, 16))
elif x[:1] == "0":
    print(int(x, 8))
else:
    print(int(x))