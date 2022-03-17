# 대표 문제1
문제 핵심 포인트: 이동할 예정인 좌표 nx,ny와 실제 이동한 위치 x,y 구분
```python
n = int(input())
plans = input().split()
x,y = 1,1
moveType = ['L','R','U','D']
dirX = [0,0,-1,1]
dirY = [-1,1,0,0]

# 이동 계획을 하나씩 확인
for p in plans:
  # 이동 후 좌표 구하기
  for i in range(len(moveType)):
    if p == moveType[i]:
      nx = x + dirX[i]
      ny = y + dirY[i]
  # 공간을 벗어나는 경우 무시
  if nx<1 or ny<1 or nx>n or ny>n:
    continue
  # 이동 수행
  x, y = nx,ny

print(x,y)
```

# 문제 1 - 시각
