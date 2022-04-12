## 1. DP 풀이

# 1) 테이블 정의하기 
  # dp[i]=> i를 1로 만들기 위해 필요한 "연산 사용 횟수의 최솟값"

# 2) 점화식 찾기 
  # dp[1]~dp[11]까지 모두 알고 있다고 생각해보면 쉬움
  # dp[12]=min(dp[11]+1,dp[4]+1,dp[6]+1)

# 3) 초기값 정의하기
  # dp[1]=0

n = int(input())
dp = [0]*(n+1)
dp[1]=0

for i in range(2,n+1):
  # 주의) 3,2로 나누어 떨어질 때만 나눠야 하기에 if문 이용
  dp[i]=dp[i-1]+1
  if i%2==0:
    dp[i]= min(dp[i],dp[i//2]+1) 
    # 주의) min 괄호 연산 끝에 +1 을 하면, 이미 연산 수행했던 것을 추가로 +1 해서 결과값이 다르게 나온다.
  if i%3==0:
    dp[i]= min(dp[i],dp[i//3]+1)

print(dp[n])

## BFS 풀이