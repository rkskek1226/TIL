[오버로딩 vs 오버라이딩](#오버로딩overloading-vs-오버라이딩overriding)

[디폴트 값](#디폴트-값default-value)

[인라인 함수](#인라인inline-함수)

[이름 공간](#이름-공간namespace)

[참조자](#참조자reference)

[동적 할당](#동적-할당)

[접근제어 지시자](#접근제어-지시자)

[const 함수](#const-함수)

[생성자와 소멸자](#생성자constructor와-소멸자destructor)

[멤버 이니셜라이저](#멤버-이니셜라이저member-initializer)

[객체 배열 vs 객체 포인터 배열](#객체-배열-vs-객체-포인터-배열)

[this 포인터](#this-포인터)

<br/>

#### 오버로딩(Overloading) vs 오버라이딩(Overriding)

* 오버로딩

* * 함수의 이름은 같지만 매개변수의 자료형이나 개수가 달라 이름을 재사용하는 것
  * C와는 달리 호출할 함수를 찾을 때 함수의 이름과 매개변수 선언을 보고 찾음
  * C는 함수의 호출할 함수를 찾을 때 함수의 이름만 사용

  ```c++
  int func(int n){cout<<n<<endl;}
  int func(int n1, int n2){return n1 + n2;}
  ```

* 오버라이딩

* * 상속 관계에서 자식 클래스의 함수가 부모 클래스의 함수를 재정의하는 것

  ```c++
  class A
  {
    private:
    	int n;
    public:
    	A(int num) : n(num){}
    	void Show(){cout<<n<<endl;}
  };

  class B : public A
  {
    private:
    	int m;
    public:
    	B(int n, int m) : A(n), m(m){}
    	void Show()
      {
        A::Show();   // 오버라이딩
        cout<<B<<endl;
      }
  };
  ```

  ​

<br/>

#### 디폴트 값(Default Value)

* 함수의 매개변수에 기본적으로 설정되어 있는 값
* 함수에 디폴트 값이 설정되어 있으면 인자 전달 시 왼쪽부터 채워져 나감
* 함수에 디폴트 값을 설정할 때 오른쪽부터 값을 채워야 함

```c++
int Adder(int n1=10, int n2=20, int n3=30){}   // 가능
int Adder(int n1, int n2=20, int n3=30){}   // 가능
int Adder(int n1=10, int n2, int n3){}   // 불가능
```

<br/>

#### 인라인(inline) 함수

* 매크로 함수를 기반으로 일반 함수처럼 정의가 가능한 함수
* 매크로 함수는 전처리기가 처리하지만 inline 함수는 컴파일러가 처리해 컴파일러가 판단하기에 성능상 해가 된다면 키워드 무시
* 인라인 함수는 자료형에 의존적이게 되어 템플릿을 사용해 해결

```c++
inline int SQUARE(int x){return x*x;}

template <typename T>
inline T SQUARE(T x){return x*x;}

cout<<SQUARE(5)<<endl;
cout<<SQUARE(5.5)<<endl;
```

<br/>

#### 이름 공간(namespace)

* 특정 영역에 이름을 붙여 충돌을 방지하는 방법으로 범위지정 연산자(scope resolution operator)인 ::를 사용

```c++
namespace AAA
{
  void func(void){}
}

namespace BBB
{
  void func(void){}
}

namespace CCC
{
  void func(void){}
}

AAA::func();
BBB::func();
using CCC::func;
func();
```

* ::은 같은 공간에서 지역변수와 전역변수의 이름이 같을 때 전역변수에 접근가능하게 함

```c++
int n=10;

void func(void)
{
  int n=20;   // 지역변수
  n += 10;   // 지역변수 n의 값 증가
  ::n += 20;   // 전역변수 n의 값 증가
}
```

<br/>

#### 참조자(Reference)

* 자신이 참조하는 변수를 대신할 수 있는 또 하나의 이름
* 선언과 동시에 초기화해야하고 참조 대상을 바꾸는 것을 불가능

```c++
int n1 = 100;
int &n2 = n1;

n2 = 200;
cout<<n1<<n2;   // 200, 200이 출력됨
```

```c++
void swap(int &ref1, int &ref2)
{
  int tmp = ref1;
  ref1 = ref2;
  ref2 = tmp;
}

int n1 = 10;
int n2 = 20;

swap(n1, n2);
cout<<n1<<n2;   // 20, 10이 출력됨
```

<br/>

#### 동적 할당

* malloc()과 free()를 대신해 new와 delete를 사용
* malloc()은 할당할 크기를 바이트 단위로 전달해야하고 반환형이 void 포인터이기때문에 형 변환을 해야했지만 new는 이럴 필요 없음

```c++
int *ptr1 = new int;
double *ptr2 = new double;
int *arr1 = new int[3];
double *arr2 = new double[7];
delete ptr1;
delete ptr2;
delete []arr1;
delete []arr2;
```

<br/>

#### 접근제어 지시자

* public : 어디서든 접근 가능
* protected : 상속관계에서는 접근 가능
* private : 클래스 내에서만 접근 가능

<br/>

#### const 함수

* const가 선언된 함수 내에서는 멤버 변수에 저장된 값을 변경하지 못함
* const 함수 내에서는 const가 아닌 함수를 호출하지 못함
* const 참조자가 참조하는 함수를 호출할 때 해당 함수가 const 함수가 아니면 호출하지 못함

```c++
class simple
{
  private:
  	int n;
  public:
  	int GetNum(){return n;}
  	void ShowNum() const {cout<<GetNum();}   // const 함수 내에서는 const가 아닌 함수를 호출하지 못하므로 에러
};

class easy
{
  private:
  	int n;
  public:
  	void InitNum(const simple &s){n = s.GetNum();}   // const 참조자가 호출하는 함수가 const가 아니므로 에러
};
```

<br/>

#### 생성자(Constructor)와 소멸자(Destructor)

* 생성자

* * 객체의 초기화 수행

* * 객체 생성시 한번만 호출
  * 오버로딩과 디폴트 값 설정이 가능
  * 생성자를 정의하지 않는다면 디폴트 생성자가 호출됨

  ```\c++
  SimpleClass sc1(100);   // 가능
  SimpleClass *ptr1 = new SimpleClass(100);   // 가능
  SimpleClass sc2;   // 가능
  SimpleClass *ptr2 = new SimpleClass;   // 가능
  SimpleClass *ptr3 = new SimpleClass();   // 가능
  SimpleClass sc3();   // 불가능
  ```

* 소멸자

* * 생성자에서 할당한 자원을 소멸하는데 사용(생성자에서 new 연산자를 사용해 메모리를 할당받았다면 delete 연산자를 사용해 메모리 해제를 수행)

* * 클래스 이름 앞에 ~가 붙는 형태로 반환형이 선언되지 않고 실제로 반환하지도 않음
  * 오버로딩과 디폴트 값 설정이 불가능
  * 객채 소멸 과정에서 자동으로 호출되고 소멸자를 정의하지 않는다면 디폴트 소멸자가 호출됨

  ```c++
  class Person
  {
    private:
    	char *name;
    public:
    	Person(char *myname)
      {
        int len = strlen(myname) + 1;
        name = new char[len];
        strcpy(name, myname);
      }
    	~Person()
      {
        delete []name;
      }
  };
  ```

<br/>

#### 멤버 이니셜라이저(Member Initializer)

* 객체의 멤버 변수를 초기화하는 방법에는 생성자와 멤버 이니셜라이저가 있음
* :를 사용해 멤버 변수 초기화 수행
* 이니셜라이저는 생성자보다 성능상 이점이 있음(이니셜라이저는 선언과 동시에 초기화가 이루어지는 형태로 바이너리 코드가 생성됨)

```c++
class Simple
{
  private:
  	int num1;
  	int num2;
  public:
  	Simple(int n1, int n2) : num1(n1){num2=n2;}   // 이니셜라이저
};
```

```c++
class Point
{
  private:
  	int xpos;
  	int ypos;
};

class Rectangle
{
  private:
  	Point upLeft;
  	point lowRight;
  public:
  	Rectangle(int x1, int y1, int x2, int y2) : upLeft(x1, y1), lowRight(x2, y2){}   // 이니셜라이저
};
```

<br/>

#### 객체 배열 vs 객체 포인터 배열

* 객체 배열

* * 객체로 이루어진 배열

  ```c++
  Simple arr[10];
  arr[1].OOO;   // .을 이용해 멤버 함수 접근
  ```

* 객체 포인터 배열

* * 객체의 주소 값 저장이 가능한 포인터 변수로 이루어진 배열

  ```c++
  Simple *ptr[10];
  ptr[1]->OOO;   // ->를 이용해 멤버 함수 접근
  ```

<br/>

#### this 포인터

* 자신을 가리키는 포인터

```c++
class Simple
{
  private:
  	int num;
  public:
  	Simple(int n) : num(n){}
  	void Show(){cout<<num<<endl;}
  	Simple *GetThisPointer(){return this;}   # 포인터를 반환하는 함수
};

int main()
{
  Simple s1(100);
  Simple *ptr1 = s1.GetThisPointer();
  ptr1->Show();   // 100이 출력됨
}
```

```c++
class Number
{
  private:
  	int num;
  public:
  	Number(int num){this->num = num;}   // this->num은 지역 변수 num이 아닌 멤버 변수 num을 의미
  	void Show(){cout<<this->num<<endl;}   // 멤버 변수 num을 출력
};
```

