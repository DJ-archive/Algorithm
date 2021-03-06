## 피보나치 수열
* 탑다운 다이나믹 프로그래밍 (python)
    * 재귀 
```python
# 99번째 피보나치 수 구하기

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0]*100

def fibo(x):
    # 호출되는 함수 확인해보기
    print('f('+str(x)+')',end=' ')
    # 종료조건
    if x==1 or x==2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x]!=0:
        return d[x]
    # 아직 계산되지 않은 문제라면 피보나치 점화식
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))
```

* 보텀업 다이나믹 프로그래밍 (python)
  * 반복문

```python
d= [0]*100

# 전제조건
d[1]=1
d[2]=1
n = 99

# 피보나치 함수 반복문으로 구현
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]

print(d[n])
```

## 접근 방법
* 주어진 문제가 다이나믹 프로그래밍 유형임을 파악하는 것이 중요
* 가장 먼저, 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 검토 후 다이나믹 프로그래밍 고려하기.
* 일단 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤에 (탑다운) 작은 문제에서 구한 답이 큰 문제에서 그래도 사용될 수 있으면, 코드를 개선하는 방법 사용
* 일반적으로는, **기본 유형** 의 DP 문제가 출제되는 경우가 많다.
  * 점화식 떠올리기가 중요 (반복 연습 필요)

## 문제. 개미 전사
```python
n = int(input())
wh = list(map(int,input().split()))

# 보텀업 방식
dp = [0]*100 # n 최댓값=100

dp[0]=wh[0]
dp[1]=max(dp[0],wh[1])

for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+wh[i])

print(dp[n-1]) # 주의
```

## 문제. 효율적인 화폐 구성

* d[i]= 금액 i를 만들 수 있는 최소한의 화폐 갯수
* k = 각 화폐의 단위 
* 점화식 d[i]
  * k를 하나씩 돌면서, d[i-k]가 존재하는 경우, d[i]=min(d[i],d[i-k]+1)
  * d[i-k]가 존재하지 않는 경우, d[i]=INF
* O(N*M) 복잡도 (이중 for문); 값 갱신

```python
n,m = map(int,input().split())
arr = [] # 화폐 단위
for i in range(n):
  arr.append(int(input()))
# 최솟값 문제에서, 불가능하다는 의미로 10001(최대 화폐값보다 큰 값;INF 대체) 사용
d=[10001]*(m+1) 

d[0]=0
for i in range(n):
  for j in range(arr[i],m+1):
    if d[j-arr[i]]!=10001: # (i-k)원을 만드는 방법이 존재할 경우
      d[j]=min(d[j],d[j-arr[i]]+1)

if d[m]==10001:
  print(-1)
else:
  print(d[m])
```
    
    
      
