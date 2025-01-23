from collections import deque
def solution(maps):
    rows, cols = len(maps), len(maps[0])
    ways = [(1,0),(0,1),(0,-1),(-1,0)]
    now = [(row, m.index('S')) for row,m in enumerate(maps) if 'S' in m][0]
    now = (now[0],now[1],0)
    
    def find_LE(tg):
        visited = [[i for i in m] for m in maps]
        visited[now[0]][now[1]] = 'X'
        queue = deque([now])
        
        while queue:
            x,y,v = queue.popleft()
        
            for dx, dy in ways:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and visited[nx][ny] != 'X':
                    if visited[nx][ny] == tg: return (nx,ny,v+1)
                    queue.append((nx,ny,v+1))
                    visited[nx][ny] = 'X'
                    
        return -1
    
    now = find_LE('L')
    if now == -1 : return -1
    now = find_LE('E')
    if now == -1 : return -1
    
    return now[2]