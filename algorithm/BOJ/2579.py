# 처음 내 풀이

# dp[i]=> i번째 계단까지의 총 점수의 최댓값
# dp[i]
  # i-3까지 + i번째 점수 + i-1번째 점수
  # i-2까지 + i번째 점수
  # max로 구현
# 초깃값 1,2,3 주의

n = int(input())
stairs = [0 for _ in range(n+3)]
for i in range(1,n+1):
  stairs[i] = int(input())
  
# 주의)) dp 테이블 인덱스를 3까지 설정했는데, n+3이상이 아니면, n=1일 경우 해당 값이 없게 된다. 
dp=[0]*(n+3)
dp[1]= stairs[1] 
dp[2]= stairs[1]+stairs[2]
dp[3] = max(stairs[2]+stairs[3],stairs[1]+stairs[3])

for i in range(4,n+1):
  dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i])
  
print(dp[n])


# 이차원 배열 풀이

# d[i][j] = 현재까지 j개의 계단을 연속해서 밟고 i번째 계단까지 올라섰을 때, 점수 합의 최댓값. 단, i번째 계단은 반드시 밟아야 함.
# d[k][1] => k번째까지 연속 1번 밟았으니, k-2가 전 단계 계단.
    # d[k][1] = max(d[k-2][1],d[k-2][2])+s[k]
    # d[k][2] = d[k-1][1]+s[k]
    # max 계산
# 초기값 => d[1][1]=s[1],d[1][2]=0, d[2][1]=s[2], d[2][2]=s[1]+s[2]

