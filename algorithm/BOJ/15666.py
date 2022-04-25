# 백트래킹 n과 m(12) - 마지막 문제

# 본인 중복 가능, 하지만 그 전 idx 불가능 (본인 이상)
# sibling 불가능 > pre값 저장

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = []

def bt(idx):
  pre = 0
  if len(answer)==m:
    print(' '.join(map(str,answer)))
    return
  for i in range(idx,len(arr)):
    if pre == arr[i]: continue
    answer.append(arr[i])
    pre = arr[i]
    bt(i)
    answer.pop()
bt(0)
