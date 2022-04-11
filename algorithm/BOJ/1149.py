# 색에 대한 데이터 필요
  # d[i][0] = i번째까지의 집을 칠하는데 드는 비용의 최솟값, 단 i번째 집은 빨강색
  # d[i][1] = 동일, 단 i번째 집은 초록
  # d[i][2] = 동일, 단 i번째 집은 파랑

# d[i][0] = min(d[i-1][1],d[i-1][2])+R(i)

n = int(input())
colors = [[0,0,0] for _ in range(n+1)] # 주의) 미리 값 할당해야 함 (index 에러)
for i in range(1,n+1):
  rgb = list(map(int,input().split()))
  colors[i] = rgb

d = [[0]*3 for i in range(n+1)]
d[1][0]=colors[1][0]
d[1][1]=colors[1][1]
d[1][2]=colors[1][2]

for i in range(1,n+1):
  d[i][0]=min(d[i-1][1],d[i-1][2])+colors[i][0]
  d[i][1]=min(d[i-1][0],d[i-1][2])+colors[i][1]
  d[i][2]=min(d[i-1][0],d[i-1][1])+colors[i][2]

answer = min(d[n][0],d[n][1],d[n][2])
print(answer)