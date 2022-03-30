## 예시 그래프
![bfs](https://user-images.githubusercontent.com/58822617/160392688-c8b4fd16-63e0-49ac-af15-b1b140867f44.PNG)

# DFS: 깊이 우선 탐색
## 구현
```python
# 각 노드가 연결된 정보를 표현 
graph = {
  1: [2,3,8],
  2: [1,7],
  3: [1,4,5],
  4: [3,5],
  5: [3,4],
  6: [7],
  7: [2,6,8],
  8: [1,7]
}

# 각 노드가 방문된 정보 
visited = [False]*9

def dfs(graph,v,visited):
  # 현재 노드 방문 처리
  visited[v]=True
  print(v,end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph.get(v):
    if not visited[i]:
      dfs(graph,i,visited)
        
dfs(graph,1,visited)
# 1 2 7 6 8 3 4 5
```

# BFS: 너비 우선 탐색
## 구현 


```python
from collections import deque

# 각 노드가 연결된 정보를 표현 
graph = {
  1: [2,3,8],
  2: [1,7],
  3: [1,4,5],
  4: [3,5],
  5: [3,4],
  6: [7],
  7: [2,6,8],
  8: [1,7]
}

# 각 노드가 방문된 정보 
visited = [False]*9

def bfs(graph,start,visited):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  #큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    # 아직 방문하지 않은 인접 원소들 큐에 삽입
    for i in graph.get(v):
      if not visited[i]:
        queue.append(i)
        visited[i]=True

bfs(graph,1,visited)
      
## 1 2 3 8 7 4 5 6
```

# 문제 1 : 음료수 얼려먹기
```python
n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# 범위 > n,m / i,j 오타 조심!!
def dfs(x,y):
  if x<0 or x>= n or y<0 or y>=m or \ 
  graph[x][y]==1:
    return 

  if graph[x][y]==0:
    # 방문 처리
    graph[x][y]=1 # == 로 실수!!
    # 동서남북 탐색
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)

count = 0
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      dfs(i,j)
      count += 1

print(count)
```

# 문제 2 : 미로탈출
```python
from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))
# 이동할 상하좌우 
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
  # 목표 위치 값 반환
  return graph[n-1][m-1]

print(bfs(0,0))
```
# BOJ
```python
from collections import deque
n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
count = 0 # 단지 수
hslist  = [] # 단지별 집 수를 담을 리스트

def bfs(x,y):
  houseN = 1 # 단지별 집 수
  queue = deque()
  queue.append((x,y))
  graph[x][y]=0 # 방문처리
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      if graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:
        queue.append((nx,ny))
        graph[nx][ny]=0 # 방문처리
        houseN += 1
  hslist.append(houseN)

for i in range(n):
  for j in range(n):
    if graph[i][j]==1:
      bfs(i,j)
      count += 1
      
print(count)
hslist.sort() # 문제 조건 잘 보기!!!!!!
for x in hslist:
  print(x)
```