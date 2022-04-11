# 하노이탑

# a=start: 시작번호 b=end:목적지번호 n:원판의 개수
  
# 1.base condition: n==1이면 a에서 b로 간다
# 2. 재귀함수 조건(귀납적 사고): n번째 판이 b로 가기 위해서 필요한 귀납적 접근
  # n-1개가 a에서 (6-a-b)로 이동
  # n번째 원판을 a에서 b로 이동시킨다
  # n-1개 원판을 (6-a-b)에서 b로 이동시킨다

def hanoi(n,start,end): 
  if n==1:
    print(start,end)
    return
  hanoi(n-1,start,6-start-end)
  print(start,end)
  hanoi(n-1,6-start-end,end)

n=int(input())
print(2**n-1)
hanoi(n,1,3)