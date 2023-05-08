import sys
input = sys.stdin.readline

n, k = map(int, input().split())

q = []
visited = [0]*200001
q.append(n)
visited[n] = 1
temp = []
ans = 0
if n == k:
    print(0)
else:
    while True:
        ans += 1
        while q:
            now = q.pop()
            if 0 <= now*2 <= 100000:
                if not visited[now*2]:
                    temp.append(now*2)
                    visited[now*2] = 1
            if 0 <= now+1 <= 100000:
                if not visited[now+1]:
                    visited[now+1] = 1
                    temp.append(now+1)
            if 0 <= now-1 <= 100000:
                if not visited[now-1] and now-1 >= 0:
                    visited[now-1] = 1
                    temp.append(now-1)
            if k in temp:
                print(ans)
                exit(0)
        # if k in temp:
        #     print(ans)
        #     break
        q.extend(list(set(temp)))
        temp = []