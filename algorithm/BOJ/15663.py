# 백트래킹 N과 M(9)
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited =[False for _ in range(n)]
answer = []

def bt():
  pre = 0
  if len(answer)==m:
    print(' '.join(map(str,answer)))
    return
  for i in range(len(arr)):
    if visited[i]: continue
    if pre == arr[i]: continue
    answer.append(arr[i])
    visited[i]=1
    pre = arr[i]
    bt()
    answer.pop()
    visited[i]=0

bt()

# pre가 필요한 이유 (sibling)
# visited가 필요한 이유
