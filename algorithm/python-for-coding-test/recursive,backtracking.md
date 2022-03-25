# 기본 자료구조 알고가기 (Stack, Queue)
## 스택
* 선입후출 방식 (입구와 출구가 같은 형태)
* 파이썬에서는 별도의 라이브러리 호출 없이, list 사용. O(1)
    * list append, pop 함수는 맨 오른쪽 값(마지막에 들어온 값)을 더하고 빼기 때문. 
```python
stack = []
stack.append(5)
stack.append(2)
stack.pop()
stack.append(3)

# Slicing[start:stop:step]
print(stack[::-1]) # 리스트 뒤집기 > 최상단 원소부터 출력
    ## 3 5
print(stack) #최하단 원소부터 출력
    ## 5 3
```
* 자바: stack 라이브러리 사용
```java
import java.util.*;
class Main {  
  public static void main(String args[]) { 
    Stack<Integer> s = new Stack<>();

    s.push(5);
    s.push(2);
    s.pop();
    s.push(3);

    // 스택의 최상단 원소부터 출력
    while(!s.empty()){
      System.out.print(s.peek()+" ");
      s.pop();
    }
  } 
}
```
## 큐
* 선입선출 방식 (입구와 출구가 모두 뚫려 있는 터널과 같은 형태)
    * 대기열
* 파이썬 deque 라이브러리 활용. O(1)

```python
from collections import deque

#큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(1)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

## deque([3, 1])
## deque([1, 3])
```
* 자바 : LinkedList의 Queue 라이브러리 사용
```java
import java.util.*;
class Main {  
  public static void main(String args[]) { 
    Queue<Integer> q = new LinkedList<>();

    q.offer(5);
    q.offer(2);
    q.offer(3);
    q.poll(); 
    // poll(): 먼저 들어온 것들을 꺼내고, 반환까지 한다
    q.offer(1);
    q.poll();

    // 먼저 들어온 원소부터 추출
    while(!q.isEmpty()){
      System.out.print(q.poll()+" ");
    }
  } 
}

//3 1
```
# 재귀 함수(Recursive Function)
* [**절차지향적 사고가 아닌, 귀납적 사고를 할줄 알아야 쉽게 풀 수 있다**](https://www.youtube.com/watch?v=8vDDJm5EewM)
* 하나의 함수에서 자기 자신을 다시 호출해 작업을 수행하는 알고리즘
* 재귀 함수의 종료 조건을 반드시 명시해야 한다.
    * 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출되어, 최대 재귀 깊이 초과 메시지가 출력될 수 있다. (오류메시지와 함께 종료)
* 종료 조건을 포함한 재귀 함수 예제

```python
def recursive_function(i):
  # 100번째 호출을 했을 때 종료되도록 종료 조건 명시 
  if i==100:
    return
  print(i,'번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
  recursive_function(i+1)
  print(i,'번째 재귀함수를 종료합니다.')

recursive_function(1)
```
> 메서드는 stack 방식으로 호출된다! <br>
위의 코드 결과 참조


## 팩토리얼 구현 예제
```python
def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)

print(factorial_recursive(5))
```
## 최대공약수 계산 (유클리드 호제법)

> 유클리드 호제법 <br> 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.

 ```python
 n,m = map(int,input().split())

def GCD(n,m):
  if n%m==0:
    return m
  else:
    return GCD(m,n%m)

print(GCD(n,m))
```

* 재귀함수를 잘 활용하면, 복잡한 알고리즘을 간결하게 작성할 수 있다. 
* 하지만, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있고 **모든 재귀합수는 반복문을 이용하여 동일한 기능을 구현할 수 있기** 때문에 신중하게 사용해야 한다.
* 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
    * 따라서 스택을 사용해야할 때, 구현상 **스택 라이브러리 대신에 재귀 함수를 이용**하는 경우가 많음

### [BOJ 하노이탑](https://www.youtube.com/watch?v=8vDDJm5EewM)
```python
# a=start: 시작번호 b=end:목적지번호 n:원판의 개수
  
# 1.base condition: n==1이면 a에서 b로 간다
# 2. 재귀함수 조건(귀납적 사고): n번째 판이 b로 가기 위해서는,
  # n-1개가 a에서 (6-a-b)로 간다
  # n번째 원판을 a에서 b로 간다
  # n-1개 원판을 (6-a-b)에서 b로 간다

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
```
# 백트래킹(Backtracking)
* 백트래킹은 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기(Backtrack)해 정답을 찾아가는 범용적인 알고리즘
* DFS는 백트래킹의 골격을 이루는 알고리즘
* 제약 충족 문제(Constraint Satisfaction Problem)에 유용
* 브루트포스와 유사하나, 한번 방문 후 가능성이 없는 경우에는 즉시 후보를 포기한다는 점에서 매번 같은 경로를 방문하는 브루트 포스보다는 훨씬 우아한 방식
> 제약 충족 문제: 수많은 제약 조건을 충족하는 상태를 찾아내는 수학 문제 <br> ex. 수도쿠, 십자말 풀이, 8퀸 문제, 4색 문제 문자열 파싱, 조합 최적합 등