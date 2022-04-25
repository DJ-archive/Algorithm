# 백트래킹 N과 M(10)

# sibling 중복 (x) > pre 이용해서, 같은 계층일 경우 중복되는 값 제거 
# 전 idx (x) > visited 말고 부모에서 자식에게 idx 넘겨주어 잡아내기

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
    bt(i+1)
    answer.pop()

bt(0)