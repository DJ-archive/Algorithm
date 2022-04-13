# 0-1 knapsack
n,k = map(int,input().split()) 
# p=가치
# d[i][w]= i번째의 item까지 고려하고 무게한도가 w일 때 얻을 수 있는 optimal profit
# d[i][w]=>
  # 1) i번째 물건이 들어가긴 할 경우, 그 전까지의 경우의 수와 전 물건 + 지금 물건 중 최댓값 고르기
    # w(i)<= w, max(d[i-1][w-wi]+pi,d[i-1][w])
  # 2) 안들어갈 경우, d[i-1][w]

d=[[0 for _ in range(k+1)] for _ in range(n+1)]
bp = [(0,0)]
for i in range(n):
  w,v = map(int,input().split())
  bp.append((w,v))
# bp.sort(key=lambda x:x[0]) 
# d 0행 혹은 0열들은 0으로 이미 초기화 되어 있음
for i in range(1,n+1):
  for j in range(1,k+1):
    if bp[i][0]<=j:
      d[i][j]=max(d[i-1][j-bp[i][0]]+bp[i][1],d[i-1][j])
    else:
      d[i][j]=d[i-1][j]
print(d[n][k])