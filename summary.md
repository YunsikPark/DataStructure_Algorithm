# data structure & algorithm

> 양태환 강사     
> ythwork83@gmail.com


---

컴퓨터공학(ComputerScience)의 5대과목: 

프로그래밍언어 자료구조 알고리즘 CPU OS

어샘블리를 알면 내부 구조를 잘 알 수 있다.

---

##### Foundation Knowledge Quiz

- **Recursion, Index, Sort**. Binary Search
- **Stack** / Heap
- **Process / Thread**
- **Call by Value:값에의해 호출, 인자를 전달할 때 값으로 전달(인자를 복사) / Call by Reference(주소값에 의해 호출, 인자를 전달할 때 참조로 전달)**
	- *python은 Call by Assignment(처음에는 참조형이지만 새롭게 할당을 하면 참조형이 끊어진다. 따라서 할당에 의해 전달하기 때문에 Assignment라고 한다)*
	- immutable: 튜플...
	- mutable: 딕셔너리...

- **Native Code**
- MVC Architecture
- **Write simple text-based games**

---

## 자료 구조의 구성
> 자료구조 : 데이터를 어떤 구조로 저장하고 탐색해야 가장 효율적인가? 

> 알고리즘 : 문제를 해결하는 방법론

> 자료구조의 알고리즘 : **데이터를 저장하고 탐색하는 방법**에 대한 고민들

> 자료구조를 이용한 알고리즘 : **자료구조를 이용**해 어떤 문제를 해결하는 것

1. Insert : 데이터를 어떻게 저장할 것인가?
2. Search : 데이터를 어떻게 탐색할 것인가?
3. Delete : 필요 없어진 데이터를 어떻게 지울 것인가?

## Array와 Linked List

1. 배열의 원리

> 배열은 동일한 자료(형)들을 가진 변수들의 모음

- 가변 배열 : 배열의 길이가 변하는 배열 / 하지만 배열은 원래 길이를 바꿀 수 없다.?
- 어마어마한 리소스 낭비
- 길이가 4인 배열은 그대로 두고 길이가 6인 배열을 따로 할당 후 (길이가 6인 메모리가 있는지 탐색이 이루어져야함) 데이터의 복사가 이루어짐

2. linked List

- 길이가 4인 링크드 리스트 만약 길이가 6인 저장공간이 필요하다면 
- 탐색, 할당, 복사, 삭제등의 리소스 낭비가 전혀 없다



데이터를 추가하거나 삭제하는 경우가 거의 없는데 데이터의 접근이 빈번할 때 **배열**을 쓴다
접근을 잘하지 않지만 자주 추가하거나 자주 삭제할 때 **Linked List**를 사용한다.

배열은 메모리에 순차적 할당이 된다.
배열은 페이지라고 부를때 순차적으로 보강을해서 빠르다
링크드 리스트는 참조로 가기 때문에 힙(Heap)에 할당이 되고 
데이터를 순회할 때 자료가 없으면 다음 페이지를 다시 순회하여 순회 할 때마다 계속 바뀌게 된다 그러므로 배열을 쓸 수 있는 상황이라면 배열을 쓰는게 좋다.




## data structure

### recursion (재(다시 재)귀(돌아올 귀)함수)

- factorial

```
def factorial(n):
    # 탈출조건
    if n <= 1:
        return 1

    return n*factorial(n-1)

if __name__ == "__main__":
    n = 3
    res = factorial(n)
    print("The factorial of {} is {}".format(n, res))

```

- fibonacci

```
# fibonacci

def fibo(n):
    if n == 0 or n == 1:
        return 1
    result = fibo(n-2) + fibo(n-1)
    return result

if __name__ == "__main__":
    n = 10
    for i in range(n):
        print(fibo(i), end=' ')

```
```
# fibonacci generator

def fibo_gen(n):
    a = b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    f = fibo_gen(10)
    for i in range(10):
        print(next(f), end=' ')

```

- hanoi tower

```
def hanoi(num, _from, _by, _to):
    # 탈출조건
    if num == 1:
        print("{}에서 {}로 {} 번째 원반 이동".format(_from, _to, num))
        return

    hanoi(num-1, _from, _to, _by)
    print("{}에서 {}로 {}번째 원반 이동".format(_from, _to, num))
    hanoi(num-1, _by, _from, _to)

if __name__ == "__main__":
    while 1:
        numOfTray = int(input("원반의 개수를 입력하세요!(종료:0):"))
        if numOfTray == 0:
            break
        hanoi(numOfTray, 'A', 'B', 'C')
```

코루틴 공부하기
*while문으로 해결이 가능하다면 사실상 재귀함수는 쓰지 않는게 좋다*

### intro

- linear search_선형탐색

```
def linear_search(data, target):
    for idx in range(len(data)):
        if data[idx] == target:
            return idx
    return None


if __name__ == "__main__":
    data = [i for i in range(10)]

    target = 4
    idx = linear_search(data, target)

    if idx == None:
        print("{}이 존재하지 않습니다".format(target))
    else:
        print("찾는 데이터의 인덱스는 {}이고 데이터는 {}입니다.".format(idx, data[idx]))

```

- binary search_이진탐색(최악의 경우를 성능지표로 삼는다)

```
def binary_search(data, target):
    """
    데이터가 정렬된 상태로 전달 되어야 합니다.
    """
    # data.sort()
    start = 0
    end = len(data) -1

    while start <= end:
        midpoint = (start + end) // 2
        if data[midpoint] == target:
            return midpoint
        elif target < data[midpoint]:
            end = midpoint -1
        else:
            start = midpoint + 1

    return None

if __name__ == "__main__":
    li = [i for i in range(11)]
    target = 5

    idx = binary_search(li, target)

    if idx:
        print(li[idx])
    else:
        print("There is no such data")

    print(help(binary_search))
```

- big O
	- ![image](https://apelbaum.files.wordpress.com/2011/10/yaacovapelbaumbigoplot.jpg)
	- 1. O(1): 데이터가 아무리 늘어나도 연산갯수가 늘어나지 않는다.(자주접근할때 인덱싱이 가능한 자료구조(배열)를 사용)
	- 2. O(n): 데이터가 늘어날 때 비례하며 늘어난다.
	- 3. O(log n): 무조건 로그형 그래프로 늘어난다
	- 4. O(n log n) : n제곱과 비슷한 형태를 띄지만 그렇게 기하 급수적으로 커지지 않는다.
	- 5. O(n 2제곱) : double sort가 n제곱이 나오는데 이 함수는 절대 쓰지 않는다.

> [matplotlib](https://matplotlib.org/faq/osx_framework.html)
	
	
- big O of linear search 
- big O of binary search

> 빅오_자료구조설계 할 때 매우 중요함, 빅오계산할 때 log가 나옴


### linked list

- 추상자료형(Abstract Data Type)
	- 자료구조책을 살 때 [추상자료형(ADT)](https://ko.wikipedia.org/wiki/%EC%B6%94%EC%83%81_%EC%9E%90%EB%A3%8C%ED%98%95)이 나오지 않은 책은 사지 말아야 한다.
- 함수인터페이스 목록(함수이름 + 인자목록, 반환값)

- single linked list
- 노드(node): 저장하고 싶은 데이터 / 다음노드를 가리키는 참조. 이 두가지로 구성되어 있다.
- 링크드 리스트 ADT
	- 1) append(data) -> None
	- 2) empty() - bool
		i) 비어있ㅇ면  True
		ii) 비어있지 않으면 False
	- 3) size() -> integer
	- 4) travrse(mode = 'next') -> node- 'first'->첫번째 노드   / 'next' ->                                                                                                                                                                                                                                                                                                                                                                                                                                  

	- 5) remove() -> node
- 자료구조
	- 1. insert
	- 2. search
	- 3. delete

##### python

- 생성자(constructor): 객체를 만들 때 반드시 한번은 호출해야 한다 *def \_\_init\_\_():*

- 소멸자(destructor): *def \_\_del\_\_():*

- Memory Leak : stack에 할당한 메모리는 수행된 후 지워지고, heap은 할당한 뒤 프로그래머가 직접 지워줘야하는데 이를 지우지 않을때는 수행 한 후에도 할당된 값이 메모리에 남아있는데 이를 **Memory Leak**k이라고 한다


- 컴파일언어는 code, data, heap, stack을 모두 사용하는데 파이썬과 같은 인터프리터 언어는 실행언어로 이를 모두 사용하지는 않는다. 파이썬에서 사용하는 모든 언어는 heap에 할당된다. 정확히 'private heap'


### stack, queue

- stack, queue, (Priority Queue)
	- stack : **LastInFirstOut**

	- queue : 선입선출(FirstIn,FirstOut-FAIFO)

	##### Stack ADT : 
	
	- 1. push(data) -> None:"스텍에 쌓는다"
	- 2. pop() -> data: 맨위 데이터 삭제 -> 삭제된 데이터 반환
	- 3. empty() -> bool
	- 4. peek() -> data : 삭제는 아니고 맨 위의 데이터를 반환(확인)하는것

	##### queue ADT :
	
	- 1. enqueue(data) -> None: "insert" 맨 뒤에 추가
	- 2. dequeue() -> data : 맨앞 데이터 삭제 -> 삭제된 데이터 반환
	- 3. empty() -> bool
	- 4. peek() -> data : 삭제는 하지 않고 맨 앞 데이터 반환
	
	- stack을 이용한 계산기 만들기

### tree

- binary tree
- binary search tree(BST)
- 균형 이진트리(self balancing binary search tree)-BST의 맹점 보완
	- AVL 트리
	- 2-3-4 트리
	- 블랙레드 트리



---


## algorithm

### 단순 알고리즘

1. Bubble Sort(버블정렬) - O(n^2)
2. Insertion Sort(삽입정렬)
3. Selection Sort(선택정렬)

### Divide and Conquer(분할정복기법)

> 해결할수 없는 문제를 정리(divide)해서 해결(conquer)하는 것

1. Quick Sort(퀵소트)


2. Merge Sort(머지소트)



### sorting

- bubble sort
	- 데이터의 개수가 많을 때 버블정렬은 쓰지 않는다.
	- bubble sort는 빅오의 n제곱과 같다
	- 2번의 for문을 사용하기 때문...

	```
		# import random
	#
	# source = [x for x in range(10)]
	# random.shuffle(source)
	#
	# def bubblesort(x):
	#     length = len(x)-1
	#
	#     for i in range(length):
	#         for j in range(length -i):
	#             if x[j] > x[j+1]:
	#                 x[j], x[j+1] = x[j+1], x[j]
	#                 # print(x)
	#
	#             # print(x)
	#
	#     return x
	#
	# bubblesort(source)
	#
	# print(source)
	
	def bubble_sort(data):
	    data_len = len(data)
	
	    for i in range(data_len - 1):
	        for j in range(data_len -i -1):
	            if data[j] > data[j+1]:
	                data[j], data[j+1]  = data[j+1], data[j]
	
	if __name__ == "__main__":
	    li = [2,3,5,2,3,8,6,7,10,8,1,4]
	    bubble_sort(li)
	    print(li)
	```

- quick sort
- big O of bubble sort
- big O of quick sort

---


## Interpreter Language *vs* Compiler Language

### Compiler Language:
	
- 잘못된 정의: 최종 오브젝트 코드가 기계어

- 컴파일언어는 컴파일 타일과 런타임이 존재

- 컴파일은 소스코드를 받아서 컴파일을 한다 이는 컴파일러와 어샘플러를 만든다.지금은 컴파일러와 어샘블러를 합해서 컴파일러로 통일한다. 
	- 오브젝트코드는 기계어(instruction)와 바이트코드로 구성 여기서 C 언어는 이미 기계어가 나왔기 때문에 바로 input을 .exe를 통해 런타임을 실행.
	- 바이트 코드(자바)는 VM(VirtualMachine)에서 기계어로 바뀌어 input을 .class로 받고 실행이된다.

- 즉 컴파일 언어는 컴파일 타일을 가지면 컴파일 언어로 정의한다. 컴파일러는

컴파일러 -> 바이트코드 -> vm -> 결과


### Interpreter Language: 

- 잘못된 정의: 최종 오브젝트 코드가 기계어가 아니다

- 인터프리터 언어는 오로지 런타임만 존재


- **인터프리터언어(퍄이썬)의 경우 input과 소스코드를 동시에 분석한다.**컴파일러 -> 바이트코드 ->vm -> 결과

input과 소스를 언제 받느냐에 따라 구분된다고 볼 수 있다.


#### Lexer(낱말분석)

- 프로그램언어를 처리하는 최초의 단계
- AST
- Lexer가 Parser를 가지면 컴파일


#### Parser(구문분석)

- 문장을 그것을 이루고 있는 구성 성분으로 분해하고 그들 사이의 위계 관계를 분석하여 문장의 구조를 결정하는 것을 말한다.
- C: 기계어
- Java: 바이트코드
- python : 바이트코드