x, y, w, h = map(int, input().split())

dx = w-x; dy = h-y
print(min(x, y, dx, dy))