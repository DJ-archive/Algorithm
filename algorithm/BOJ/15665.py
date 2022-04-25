# sibling 중복 x > pre값 저장하여 같은 계층 내에서 중복 값 제거
# 본인 중복은 가능 > visited 필요 x, idx 넘겨줄 필요 x
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = []

def bt():
  pre = 0
  if len(answer)==m:
    print(' '.join(map(str,answer)))
    return
  for i in range(len(arr)):
    if pre == arr[i]: continue
    answer.append(arr[i])
    pre = arr[i]
    bt()
    answer.pop()

bt()