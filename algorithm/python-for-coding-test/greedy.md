# 문제 1
## 처음 내 풀이 
* n,k 값이 작기 때문에 이렇게 모든 연산 하나씩 확인해보는 코드도 돌아가긴 하지만, 
* n 값이 더 커지면 타임에러가 날 수 있다. 

```python
N,K = map(int,input().split())
cnt = 0

while N>1:
  if N%K==0:
    N = N//K
    cnt +=1
  else:
    N -= 1
    cnt +=1

print(cnt)
```
## 시간 복잡도 O(logn) 풀이
* 가능하면 최대한 많이 나누는 작업을 통해, n이 아무리 큰 수라고 하더라도 기하급수적으로 빠르게 줄이고 시간 복잡도를 줄일 수 있음
```python
n,k = map(int,input().split())
result =0

while True:
  # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
  target = (n//k)*k #k로 나눌 수 있는 값 중 n에 가장 가까운 수
  result += n-target # '-1 연산' 횟수를 한번에 구하기
  n = target
  # N이 K보다 작을 때
  if n<k:
    break
  result += 1 # 'k 나누기' 연산 수행 횟수 
  n //= k

# 마지막 남은 수 1씩 빼거나, 한번에 다 뺐을 경우 1 더해주기
result += (n-1)
print(result)
```