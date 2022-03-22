# 대표 문제1
문제 핵심 포인트: 이동할 예정인 좌표 nx,ny와 실제 이동한 위치 x,y 구분
```python
n = int(input())
plans = input().split()
x,y = 1,1
moveType = ['L','R','U','D']
dirX = [0,0,-1,1]
dirY = [-1,1,0,0]

# 이동 계획을 하나씩 확인
for p in plans:
  # 이동 후 좌표 구하기
  for i in range(len(moveType)):
    if p == moveType[i]:
      nx = x + dirX[i]
      ny = y + dirY[i]
  # 공간을 벗어나는 경우 무시
  if nx<1 or ny<1 or nx>n or ny>n:
    continue
  # 이동 수행
  x, y = nx,ny

print(x,y)
```

# 문제 1 - 시각
완전탐색(Brute Forcing)

문제 핵심
* 파이썬 1초 연산은 2천만정도까지 가능 (>86400), 완전탐색 가능
* 삼중 for문 확인: 문자열로 합치고 해당하는 수 있는지 확인
```python
h = int(input())
cnt = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        cnt += 1
print(cnt)
```
## 자바 풀이
```java
import java.util.*;
class Main {  
  // static 함수는 인스턴스화 필요 없음
  // 시,분,초의 3 포함 여부 체크 함수
  public static boolean check(int h, int m, int s){
    if(h%10==3||m/10==3||m%10==3||s/10==3||s%10==3){
      return true;
    }
    return false;
  }
  public static void main(String args[]) { 
    Scanner sc = new Scanner(System.in);
    int h = sc.nextInt();
    int cnt = 0;
    
    for(int i=0;i<=h;i++){
      for(int j=0;j<60;j++){
        for(int k=0;k<60;k++){
          if (check(i,j,k))cnt++;
        }
      }
    } 
    System.out.println(cnt);
  } 
}
```
# 문제 2 - 왕실의 나이트
* 문자>아스키코드: ord() 함수
  * 아스키코드 > 문자: chr() 함수
* 튜플 인덱싱

```python
inputData = input()
# 행,열번호 1부터 시작하는 2차원 배열
row = int(inputData[1])
col = ord(inputData[0])-ord('a')+1 # 아스키코드 

# 튜플로 방향 묶을 수 있음(인덱싱 가능)
steps = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

cnt = 0
for step in steps:
  nrow = row + step[0]
  ncol = col + step[1]
  # 해당 위치로 이동이 불가하다면 넘어가고, 가능하면 카운트 증가
  if nrow<1 or nrow>8 or ncol<1 or ncol>8:
    continue
  cnt +=1

print(cnt)
```
## 자바풀이
```java
import java.util.*;
class Main {  
  public static void main(String args[]) { 
    Scanner sc = new Scanner(System.in);
    String input = sc.next();
    int x = input.charAt(1)-'0';
    int y = input.charAt(0) - 'a' +1;

    int[] dirX = {2,-2,2,-2,1,-1,1,-1};
    int[] dirY = {1,1,-1,-1,2,2,-2,-2};
    int cnt =0;
    for(int i=0;i<8;i++){
      int nx = x+dirX[i];
      int ny = y+dirY[i];

      if(nx>=1 && nx<=8 && ny>=1 && ny<=8){ // 반대로 해봄
        cnt++;
      }
    }
    System.out.println(cnt);
    
  } 
}
```

# 문제 3 - 문자열 재정렬

```python
# 숫자일 경우 더하고, 문자인 경우 list에 넣고 sort
inputData = input()
value =0
result = []

for i in inputData:
  if i.isalpha(): # isalpha() 함수
    result.append(i)
  else:
    value+=int(i) # 형변환 잊지 말기

result.sort()
if value != 0:
  result.append(str(value)) # 형변환

print(''.join(result)) # join
``` 