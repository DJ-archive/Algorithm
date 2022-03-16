# [MIT] 6.006: Introduction to Algorithms
[강의소개 및 자료 사이트](https://courses.csail.mit.edu/6.006/fall11/notes.shtml)
## 1. Introduction
### 극댓값 찾기
* 문제) **극댓값이 존재할 경우**, 그 값을 찾아라. 
* 전제) 좌우값보다 **같거나** 큰 경우 극댓값
    *  극댓값 정의에서 "같거나" 조건이 없다면, 극댓값이 존재하지 않을 수 있다.

### 1) 1차원의 경우


![1차원 극댓값찾기](https://user-images.githubusercontent.com/58822617/158577595-7f54fda6-c2c0-470b-8522-92ef9bcc8ce1.PNG)


b ≥ a이고 b ≥ c 이면 2번 위치가 극댓값이다. i ≥ h 이면 9번 위치가 극댓값이다.

![왼쪽부터 시작하는 경우](https://user-images.githubusercontent.com/58822617/158579823-d8de6e80-5812-4d2d-84d0-d59901b06c3f.PNG)

왼쪽 혹은 오른쪽부터 순차적으로 확인하는 경우, 평균적으로 n/2개의 원소 확인. 최악의 경우에는 n개의 원소 확인: O(n)

### 더 효율적으로 찾을 수 있을까?
### : 분할 정복 
* 문제를 작은 문제로 분할하여 문제를 해결하는 방법
* 분할 정복 알고리즘은 보통 재귀 함수(recursive function)를 통해 자연스럽게 구현된다.


![1차원 분할정복](https://user-images.githubusercontent.com/58822617/158581367-dd8911ce-f026-4fd6-bf09-a5fb5b4c43a0.PNG)

* a[n/2] < a[n/2 - 1] 이면 왼쪽 절반인 1부터 n/2-1까지 보고 극댓값을 찾는다.
* 그게 아니고 a[n/2] < a[n/2 + 1] 이면 오른쪽 절반인 n/2 + 1부터 n까지 보고 극댓값을
찾는다.
* 그것도 아니면 n/2 위치가 극댓값이다.
    * a[n/2] ≥ a[n/2 − 1]
    * a[n/2] ≥ a[n/2 + 1]

* 이를 반복한다. (재귀)