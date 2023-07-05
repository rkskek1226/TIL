[심볼릭 상수(const 상수)](#심볼릭-상수const-상수)

[형 변환](#형-변환)

[자동 형 변환](#자동-형-변환)

[명시적 형 변환](#명시적-형-변환)

[조건 연산자](#조건-연산자)

[전역 변수 VS static 변수](#전역-변수-vs-static-변수)

[Null 문자](#null-문자)

[포인터 변수](#포인터-변수)

[문자열 표현](#문자열-표현)

[더블 포인터](#더블-포인터)

[2차원 배열 이름의 포인터](#2차원-배열-이름의-포인터)

[포인터 배열](#포인터-배열)

[함수 포인터](#함수-포인터)

[void 포인터](#void-포인터)

[구조체](#구조체)

[typedef 선언](#typedef-선언)

[공용체](#공용체)

[열거형(Enumerated Type)](#열거형enumerated-type)

[동적 할당](#동적-할당)

[선행 처리](#선행-처리)

[조건부 컴파일](#조건부-컴파일conditional-compilation을-위한-매크로)

[파일 분할](#파일-분할)

<br/>

#### 심볼릭 상수(const 상수)

* 이름을 지니는 상수로 값의 변경이 불가
* 선언시 초기화해야함
* 주로 대문자로 표현하소 둘 이상의 단어를 연결할 때는 _를 활용
* const int MAX = 100;

<br/>

#### 형 변환

* 자동 형 변환과 명시적 형 변환이 있음

<br/>

#### 자동 형 변환

* 대입 연산자(=) 시행시 피연산자의 자료형이 일치하지 않을 때 왼쪽에 있는 피연산자를 대상으로 형 변환이 자동으로 이루어짐
* 데이터의 표현범위가 넓은 자료형으로의 형 변환은 손실이 발생하지 않음(double n1 = 245;)
* 데이터의 표현범위가 좁은 자료형으로의 형 변환은 손실이 발생(int n2 = 3.1415;)
* 피연산자들의 자료형이 일치하지 않아 발생하는 자동 형 변환은 데이터의 손실을 최소화하는 방향으로 진행(double n3 = 5.15 + 19;에서 int형을 double로 자동 형 변환)

<br/>

#### 명시적 형 변환

* 형 변환 연산자(type casting operator)를 이용해 강제로 형 변환 시행
```c++
  int n1 =3, n2 = 4;
  double result;
  result = (double)n1 / n2;
  // (double)n1으로 n1이 3.0이 됨
```

<br/>

#### 조건 연산자

* 삼항 연산자
* 조건 ? data1 : data2;의 형태로 조건이 참이면 data1이 반환되고 거짓이라면 data2가 반환됨
* int n3 = n1 > n2 ? n1 : n2;
* int n = (n3 > 0) ? n3 : (-1) * n3;

<br/>

#### 전역 변수 VS static 변수

* 프로그램 실행 시 메모리에 할당되고 종료시에 해제된다는 공통점이 있음
* 전역 변수는 어디서는 접근 가능하지만 static 변수는 선언된 지역 내에서만 접근 가능

<br/>

#### Null 문자

* char형 배열을 사용해 문자열을 저장할 때 '\0'을 사용해 문자열의 끝을 표현
* '\0'이 존재하면 문자열이고 존재하지 않으면 문자열이 아님
* char arr1[] = {'H', 'i', '~'};   문자 배열임
* char arr2[] = {'H', 'i', '~', '\0'};   문자열

<br/>

#### 포인터 변수

* 주소 값을 저장하는 변수
* type *ptr;   type형 변수의 주소 값을 저장하는 포인터 변수 ptr 선언한 것
* 배열의 이름은 값을 바꿀 수 없는 상수 형태의 포인터이지만 포인터 변수는 값을 바꿀 수 있는 변수
```c
  int arr[3] = {11, 22, 33};
  int *ptr = arr;
  printf("%d %d %d\n", *(ptr + 0), *(ptr + 1), *(ptr + 2));
  printf("%d %d %d\n", ptr[0], ptr[1], ptr[2]);
  printf("%d %d %d\n", *(arr + 0), *(arr + 1), *(arr + 2));
  printf("%d %d %d\n", arr[0], arr[1], arr[2]);
  // 출력 결과 모두 같음
```

<br/>

#### 문자열 표현

* 배열을 기반으로 하는 변수 형태의 문자열
* * char str1[] = "My String";
  * 배열을 기반으로 하기 때문에 문자열의 일부를 변경할 수 있음
  * 배열은 상수 형태의 포인터이므로 str1이 가리키는 대상을 변경할 수 없음
* 포인터를 기반으로 하는 상수 형태의 문자열
* * char *str2 = "Your String";
  * 문자열을 가리키는 포인터 변수이므로 문자열의 일부를 변경할 수 없음
  * str2가 가리키는 대상 문자열을 변경할 수 있음(str2 = "Out team";)

```c
  char str1[] = "My String";
  char *str2 = "Your String";
  str2 = "Out String";   // 가능
  str1[0] = 'Q';   // 가능
  str2[0] = 'Q';   // 불가능
```

  <br/>

#### 더블 포인터

* 포인터 변수를 가리키는 포인터 변수

```c
int n = 10;
int *ptr = &n;
int **dptr = &ptr;
```

<br/>

#### 2차원 배열 이름의 포인터

* 2차원 배열을 가리키는 포인터 변수

```c
int arr[3][4];
int (*ptr)[4];   // 2차원 배열 이름의 포인터로 2차원 배열의 열의 개수를 맞춰줘야 함
```

```c
int arr1[2][7];
double arr2[4][5];

void func(int (*parr1)[7], double (*parr2)[5]);
```

<br/>

#### 포인터 배열

* 포인터 변수로 이루어진 배열

```c
int n1 = 10;
int n2 = 20;
int *arr[2] = {&n1, &n2};
printf("%d\n", *arr[0]);
printf("%d\n", *arr[1]);
```

<br/>

#### 함수 포인터

* 함수의 주소 값을 저장하는 포인터 변수
* 배열의 이름이 배열의 시작 주소를 의미하듯 함수의 이름도 함수가 저장된 메모리 주소 값을 의미
* 함수 포인터의 형(type)은 반환형과 매개변수의 선언으로 결정

```c
void adder(int n1, n2){printf("%d\n", n1 + n2);}

void (*fptr)(int, int) = adder;
fptr(10, 20);
```

<br/>

#### void 포인터

* void *ptr;
* void 포인터 변수는 무엇이든 담을 수 있음(어떠한 변수의 주소 값이나 함수의 주소 값도 가능)
* void 포인터는 값의 변경이나 참조 불가능

```c
void func(void){printf("Hello");}

int n = 10;
void *ptr;
ptr = &n;
printf("%p\n", ptr);   // 변수 n의 주소 값 저장

ptr = func;
printf("%p\n", ptr);   // 함수 func의 주소 값 저장
```

<br/>

#### 구조체

* struct 키워드를 사용해 사용자 정의 자료형을 만드는 것

```c
struct person   // person이라는 이름의 구조체 정의
{
  char name[20];
  int age;
};

struct person man1;
struct person man2 = {"Jo", 20};
struct person man3[2] = {{"qwe", 30}, {"asd", 40}};
struct person *man4 = &man2;

strcpy(man1.name, "kim");
man1.age = 10;

strcpy(man4->name, "qwe");
man4->age = 30;   // (*man4).age = 30;이랑 같음
```

<br/>

#### typedef 선언

* typedef 선언은 기존에 존재하는 자료형에 새로운 이름을 부여하는 것
* typedef로 새롭게 정의되는 자료형의 이름은 주로 대문자로 시작

```c
typedef struct point
{
  int xpos;
  int ypos;
}Point;

Point p1 = {10, 20};
printf("%d %d\n", p1.xpos, p1.ypos);
```

<br/>

#### 공용체

* union 키워드 사용해 정의
* 구조체는 구조체를 구성하는 멤버가 각각 할당되지만 공용체는 멤버들 중 크기가 가장 큰 멤버 변수만 할당되고 이를 공유

```c
typedef union box
{
  int mem1;
  int mem2;
  double mem3;
}Box;

Box b1, b2;

printf("%p %p %p\n", &b1.mem1, &b1.mem2, &b1.mem3);   // 같은 값이 출력됨
printf("%d\n", sizeof(Box));   // 8이 출력됨

b2.mem1 = 20;
printf("%d\n", b2.mem1);   // mem1은 int형이고 상위 4바이트를 참조
b2.mem3 = 10.5;
printf("%d %d %g\n", b2.mem1, b2.mem2, b3.mem3);   // 쓰레기 값, 쓰레기 값, 10.5가 출력됨

```

<br/>

#### 열거형(Enumerated Type)

* enum 키워드 사용해 정의


* 저장이 가능한 값을 정수 형태로 결정

```c  
typedef enum syllable
{
  Do=1, Re=2, Mi=3
}Syllable;

Syllable tone;
for(tone=Do; tone<=Mi; tone+=1)
{
  switch(tone)
  {
    case Do:
      printf("Do");
      break;
    case Re:
      printf("Re");
      break;
    case Mi:
      printf("Mi");
      break;
  }
}
```

```c
enum color {RED, BLUE, WHITE};   // RED는 0, BLUE는 1, WHITE는 2로 결정됨
enum color {RED=3, BLUE=4, WHITE};   // RED는 3, BLUE는 4, WHITE는 5로 결정됨
```

<br/>

#### 동적 할당

* 힙 영역에 동적으로 메모리를 할당 받음
* malloc()을 통해 메모리를 할당 받고 해당 주소 값을 void 포인터 형태로 리턴
* void 포인터로는 값을 변경할 수 없어 사용하고자하는 형태로 형 변환을 해야함
* malloc()은 할당된 메모리 공간이 쓰레기 값으로 초기화되지만 calloc()은 0으로 초기화 됨
* realloc()은 할당된 메모리 크기를 재조정하는 함수

```c
#include <stdlib.h>

void *ptr = malloc(4);   // 4byte가 힙 영역에 할당되고 해당 주소를 리턴 받음
free(ptr);   // 힙 영역에 할당받은 메모리 해제

int *ptr = (int*)malloc(sizeof(int));   // 사용하고자하는 형태로 형 변환
if(ptr == NULL) {}   // 메모리 할당 실패에 따른 오류 처리
ptr = (int*)realloc(ptr, sizeof(int) * 2);
free(ptr);
```

<br/>

#### 선행 처리

* 컴파일 이전의 처리로 선행처리 명령문대로 소스코드 일부를 수정하는 작업을 수행

```c
// 대표적인 선행 처리 명령문
#include <stdio.h>
#define PI 3.14
#define SQUARE(x) x*x
#define SQUARE(x) ((x) * (x))

#define JOB(A, B) "A의 직업은 B입니다"   // 매개변수 치환이 안됨, 틀린 구문
#define JOB(A, B) #A "의 직업은 " #B "입니다"   // #을 사용해 문자열을 매개변수 치환, 맞는 구문

#define STUDENT_NUM(Y, S, P) YSP   // STUDENT_NUM(10, 60, 175) 전달 시 1060175로 치환될 것을 기대하지만 단순히 연결하는 것은 불가능
#define STUDENT_NUM(Y, S, P) Y##S##P   // ##을 사용하면 STUDENT_NUM(10, 60, 175) 전달 시 1060175로 단순히 연결시켜줌
```

* 매크로 상수
* * #define PI 3.14에서 #define은 지시자, PI는 매크로, 3.14는 매크로 몸체
  * PI라는 이름의 매크로는 상수 3.14가 됨
* 매크로 함수
* * #define SQUARE(x) x*x 처럼 동작 방식이 함수와 유사한 형태
  * 만약 SQUARE(3+2)를 수행하면 3+2*3+2가 되기때문에 SQUARE((3+2))로 작성해야함
  * 하지만 이런 형태는 사람이 주의를 해야하는 불안정한 형태
  * #define SQUARE ((x)*(x)) 처럼 인자 하나하나에 괄호를 추가하고 전체를 한번더 괄호로 묶어주는 것이 좋음
  * 자료형에 따라 별도로 함수를 정의하지 않아도 된다는 장점이 있음
  * 일반 함수보다 실행 속도가 빠름(일반 함수가 호출되면 이를 위해 스택 메모리를 할당받고 해당 위치로 이동한 후 매개변수를 전달하고 return문에 의해 값을 반환)
  * 정의하기가 까다롭고 디버깅이 어렵다는 단점이 있음
  * 작은 크기의 함수나 호출 빈도가 높은 함수를 매크로 함수로 작성하는 것이 좋음

<br/>

#### 조건부 컴파일(Conditional Compilation)을 위한 매크로

* 매크로 지시자 중 특정 조건에 따라 소스코드 일부를 삽입하거나 삭제하는 것

* #if ... #endif

* * 조건부 코드 삽입을 위한 지시자

* * ```c
    #define ADD 1
    #defind MIN 0

    #if ADD   // ADD가 참이라면 실행
    	printf("hello\n");
    #endif

    #if MIN   // MIN이 참이라면 실행
    	printf("world\n");
    #endif

    // printf("hello\n");이 실행
    ```

* #ifdef ... #endif

* * #ifdef는 특정 매크로가 정의되었는지 아닌지를 기준으로 정의되었다면 실행

  * #ifndef는 특정 매크로가 정의되었는지 아닌지를 기준으로 정의되어있지 않다면 실행

  * ```c
    #define ADD 1

    #ifdef ADD   // 매크로 ADD가 정의되었다면 실행
    	printf("hello\n");
    #endif

    #ifdef MIN   // 매크로 MIN이 정의되었다면 실행
    	printf("world\n");
    #endif

    // printf("hello\n");이 실행
    ```

<br/>

#### 파일 분할

* extern 키워드

* * 파일 분할 시 외부에 선언 및 정의되었다고 컴파일러에게 알려주는 키워드

  * ```c
    extern int num;   // num의 자료형이 int형이고 외부에 선언되었다고 컴파일러에게 알려줌
    extern void Increment(void);   // 외부에 선언되었다고 알려주는 키워드이지만 함수가 외부에 정의된 경우에는 extern 키워드 생략해도 괜찮
    ```

