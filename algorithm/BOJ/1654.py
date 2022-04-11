# 사소한 실수 조심, 이분탐색 자세히 이해하기 
import sys
input = sys.stdin.readline
k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]

start = 1 # 랜선의 길이는 1 이상이어야 함
end = max(arr)

while (start<=end):
  mid = (start+end)//2
  cnt = 0 # 카운트 갱신해야 하므로, while문 안에 넣기
  for x in arr:
    cnt += x//mid
  if cnt<n: # for 문 안에 if문 아님 (논리)
    end = mid-1
  else: # 목표 갯수보다 같거나 클 경우가 정답
    start = mid+1 

print(end) # mid가 아닌 end로 하는 이유:랜선의 최대 길이
 # ex. 603 > 200 3번 or 201 3번