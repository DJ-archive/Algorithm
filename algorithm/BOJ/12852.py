# DP 경로찾기 
  # 값 테이블(D) + 경로 복원용 테이블(pre) 추가
  # d[i] = i가 1이 되기위해 수행하는 연산 횟수의 최솟값
    # d[i]=min(d[i-1],d[i//2],d[i//3])+1 (단, 2와 3으로 나누어 떨어질 때)
  # pre[i] = i 바로 전에 최적의 i-1

n = int(input())
d=[0]*1000005
prePath=[0]*1000005
d[1]=0
prePath[1]=0

tmp = 0
for i in range(2,n+1):
  d[i]=d[i-1]+1
  tmp = i-1
  if i%2==0:
    d[i]=min(d[i],d[i//2]+1)
    if d[i]==d[i//2]+1:
      tmp = i//2
  if i%3==0:
    d[i]=min(d[i],d[i//3]+1)
    if d[i]==d[i//3]+1:
      tmp = i//3
  prePath[i]= tmp

print(d[n])
cur=n
while(True):
  print(cur,end=' ')
  if cur==1:
    break
  cur=prePath[cur]
  
  
