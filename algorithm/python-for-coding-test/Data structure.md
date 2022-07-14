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