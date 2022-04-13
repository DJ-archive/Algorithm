# 11659: 구간합 구하기 4
  # 이중 for문으로 구할 경우 O(NM) 시간복잡도
  # **prefix sum 알고리즘**
    # d[i]= a1+a2+...+ai 즉, i번째까지의 누적합
    # d[i]=d[i-1]+ai (1-indexed가 편함)
      # O(N) 
    # 이후 b번째부터 i번째까지의 구간합 구할 시, d[i]-d[b-1] 사용
      # O(1) 

n,m = map(int,input().split())
a = list(map(int,input().split()))
d=[0] # prefix_sum init

temp = 0 # 누적합 담기
for i in a:
  temp += i
  d.append(temp)
  

for i in range(m):
  a,b = map(int,input().split())
  print(d[b]-d[a-1])