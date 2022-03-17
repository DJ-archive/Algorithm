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

# 문제 2
## 내 풀이
```python
data = input()

result = 0 
for i in range(len(data)):
  d = int(data[i]) # string으로 받으므로 반드시 필요
  # 0,1일 경우 +
  if d<=1 or result<=1:
    result += d
  else:
    result *= d

print(result)
```
## 자바 풀이
```java
import java.util.*;
class Main {  
  public static void main(String args[]) { 
    Scanner sc = new Scanner(System.in);
    String str = sc.next();
    int result = 0;
    for(int i=0;i<str.length();i++){
      int num = str.charAt(i)-'0';
      if (num<=1||result<=1){
        result += num;
      }else{
        result *= num;
      }
    }
    System.out.println(result);
  } 
}
```
## 첫 항 미리 더해서 푼 답지
```python
data = input()
# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
# i 말고 알아보기 쉽게 num이라 표시함
for num in range(1,len(data)):
  if num<=1 or result<=1:
    result += num
  else:
    result *= num
print(result)
```

# 문제 3
* 잘한 점
  * 오름차순한 뒤 탐색 > 최소한 적은 사람들로 그룹을 짓게 하여 그룹 수를 최대화 하기
  * dict 컴프리헨션을 이용하여 list내의 값을 key 값으로 하고, value를 그 카운팅 값으로 설정
  * 몫, 나머지를 이용한 풀이
* 다른 점/간과한 점
  * 나는 '그룹'이 기본적으로 2명 이상인 것으로 생각하여 풀었다. > 공포도가 1인 사람도 혼자서 떠날 수 있다!
  * 굳이 dict로 바꾸지 않아도, list 안에서 문제에서 주어진 변수를 활용하여 풀 수 있다. (공포도)
  
## 내 풀이
```python
n = input()
inputList = list(map(int,input().split()))
inputList.sort()
dict = {i:inputList.count(i) for i in inputList}
sum = dict[1] # 그룹이 되지 못한 사람들 수 (공포도가 1인 사람들 수 미리 세팅)
res = 0 # 가능한 그룹 수
for k in dict.keys():
  if k>1:
    sum += dict[k]
    res += sum//k
    sum %= k
print(res)  
```
## 답지
```python
n = int(input())
data = list(map(int,input().split()))
data.sort()
grNum = 0 # 총 그룹의 수
ppCnt = 0 # 현재 그룹에 포함된 모험가의 수
for d in data: # 공포도를 낮은 것부터 하나씩 확인하여
  ppCnt+=1 # 현재 그룹에 해당 모험가를 포함시키기
  if ppCnt >= d: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성(오름차순이기에)
    # 헷갈렸던 점) ppCnt == d 조건 x 
    grNum += 1 # 총 그룹의 수 증가시키기
    ppCnt =0 # 현재 그룹에 포함된 모험가의 수 초기화
print(grNum)
```
## 자바 풀이
```java
import java.util.*;
class Main {  
  public static int n;
  public static ArrayList<Integer> arrayList = new ArrayList<>();
  public static void main(String args[]) { 
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    for(int i=0;i<n;i++){
      arrayList.add(sc.nextInt());
    }
    Collections.sort(arrayList);

    int ppCnt = 0;
    int grNum = 0;

    for(int i=0;i<n;i++){
      ppCnt +=1;
      if(ppCnt>=arrayList.get(i)){
        grNum +=1;
        ppCnt =0;
      }
    }
    System.out.println(grNum);
  } 
}
```