# 시작점이 여러개인 BFS
from collections import deque
m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
days = [[0]*m for _ in range(n)]

queue = deque()
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      queue.append((i,j))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
while queue:
  x,y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
      queue.append((nx,ny))
      graph[nx][ny]=1
      days[nx][ny]=days[x][y]+1

# days 최댓값 구하기
# graph에 0이 존재하면, -1 리턴

# 이중 for문은 break로 완전히 빠져나올 수 없음. 
    # flag 이용
flag = 1
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      flag = 0
        
max_cnt = 0     
if flag==1:
  for i in range(n):
    for j in range(m):
      max_cnt = max(max_cnt,days[i][j])
  print(max_cnt)
else: 
  print(-1)


      