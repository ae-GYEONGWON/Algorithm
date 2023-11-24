import sys
start,end = map(int, sys.stdin.readline().split(" "))

pl = [5,7,11]
for idx in range(2,5):
    for i in range(10**(idx-1),10**idx):
        k = str(i)
        pl.append(int(k+k[0:idx-1][::-1]))
        pl.append(int(k+k[::-1]))

def is_sosu(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True

pl.sort()
for num in pl:
    if start <= num <= end:
        if 12 < num:
            if is_sosu(num):
                print(num)
        else:
            print(num)
        
print(-1)
