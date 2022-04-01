from collections import deque
n,m = map(int,input().split())
graph = []
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
  queue = deque()
  area = 1
  queue.append((x,y))
  graph[x][y]=0
  
  while queue:
    x,y = queue.popleft()
    #print(x,y)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny]==0:
        continue
      else:
        queue.append((nx,ny))
        graph[nx][ny]=0
      area += 1
  
  return area

  
cnt = 0
max = 0
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      area = bfs(i,j)
      cnt += 1 # 들여쓰기 안하면 모든 i,j count
    if area > max:
      max = area

print(cnt)
print(max)