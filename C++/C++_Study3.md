[연산자 오버로딩](#연산자-오버로딩)

[대입 연산자 오버로딩](#대입-연산자-오버로딩)

[배열 인덱스 연산자 오버로딩](#배열-인덱스-연산자-오버로딩)

[스마트 포인터](#스마트-포인터smart-pointer)

[펑터](#펑터functor)

<br/>

#### 연산자 오버로딩

* 객체를 기본 자료형처럼 덧셈, 뺄셈, 곱셈, 나눗셈 같은 연산들을 가능하게 하는 것
* operator 키워드와 연산자를 묶어 함수의 이름을 정의하는 방식
* pos1 + pos2;가 pos1.operator+(pos2);와 동일한 문장
* 연산자를 오버로딩하는 방법에는 멤버 함수에 의한 연산자 오버로딩과 전역 함수에 의한 연산자 오버로딩이 있음
* 동시에 두 방법으로 연산자 오버로딩한다면 멤버 함수 기반으로 오버로딩된 함수가 전역 함수 기반으로 오버로딩된 함수보다 먼저 호출됨
* 멤버 함수에 의한 연산자 오버로딩
  * pos1 + pos2;는 pos1.operator+(pos2);로 해석됨
* 전역 함수에 의한 연산자 오버로딩
  * pos1 + pos2;는 operator+(pos1, pos2);로 해석됨

```c++
class Point
{
  private:
  	int xpos, ypos;
  public:
  	Point(int x, int y) : xpos(x), ypos(y){}
  	Point& operator++()   // 멤버 함수에 의한 연산자 오버로딩(전위 증가)
    {
      xpos += 1;
      ypos += 1;
      return *this;
    }
  	Point operator++(int)   // 멤버 함수에 의한 연산자 오버로딩(후위 증가)
    {
      Point retobj(xpos, ypos);
      xpos += 1;
      ypos += 1;
      return retobj;
    }
  	friend Point& operator--(Point &ref);   // 전역 함수에 의한 연산자 오버로딩(전위 감소)
  	friend Point& operator--(Point &ref, int);   // 전역 함수에 의한 연산자 오버로딩(후위 감소)
}

Point& operator--(Point &ref)
{
  ref.xpos -= 1;
  ref.ypos -= 1;
  return ref;
}

Point operator--(Point &ref, int)
{
  Point retobj(ref);
  ref.xpos -= 1;
  ref.ypos -= 1;
  return retobj;
}
```

* 연산자를 중심으로 피연산자의 위치가 연산의 결과에 영향을 미치지 않는다는 교환 법칙이 성립하는 연산으로는 덧셈과 곱셈이 있음
* * tmp = pos * 3;은 tmp = 3 * pos;로 구문을 작성해도 같은 결과를 내야함
  * tmp = 3 * pos;는 멤버 함수에 의한 연산자 오버로딩으로는 구현 불가능(멤버 함수에 의한 연산자 오버로딩은 객체가 연산자의 왼쪽에 와야하기 때문)
  * 이는 전역 함수에 의한 연산자 오버로딩으로 구현해야함

```c++
class Point
{
  private:
  	int xpos, ypos;
  public:
  	Point(int x=0, int y=0) : xpos(x), ypos(y){}
  	Point operator*(int times)   // 멤버 함수에 의한 연산자 오버로딩, pos * 3;이 가능
    {
      Point pos(xpos * times, ypos * times);
      return pos;
    }
  	friend Point operator*(int times, Point &ref);
};

Point operator*(int times, Point &ref)   // 전역 함수에 의한 연산자 오버로딩, 3 * pos;이 가능
{
  return ref * times;
}

int main()
{
  Point pos(1, 2);
  Point cpy;
  
  cpy = pos * 3;
  cpy = 3 * pos;
  cpy = 2 * pos * 3;
  return 0;
}
```

<br/>

#### 대입 연산자 오버로딩

* 정의하지 않으면 디폴트 대입 연산자가 실행되고 디폴트 대입 연산자는 얕은 복사를 수행
* 깊은 복사를 위해 대입 연산자를 정의하는 것이 좋음
* 대입 연산자를 정의해 깊은 복사를 수행하고 메모리 해제 연산을 수행해야함

```c++
class Person
{
  private:
  	char *name;
  	int age;
  public:
  	Person(char *_name, int _age) : age(_age)
    {
      name = new char[strlen(_name) + 1];
      strcpy(name, _name);
    }
  	/*
  	Person& operator=(const Person& ref)   // 반환형이 참조형
    {
      delete []name;
      name = new char[strlen(ref.name) + 1];
      strcpy(name, ref.name);
      age = ref.age;
      return *this;
    }
    */
  	~Person()
    {
      delete []name;
    }
};

int main()
{
  Person man1("qqq", 10);
  Person man2("www", 20);
  man2 = man1;   
  // 디폴트 대입 연산자 수행으로 2가지 문제 발생
  // 1. 문자열 "www"을 가리키는 주소 값을 잃어버려 메모리 누수 발생
  // 2. 문자열 "qqq"를 중복 소멸
}
```

* 자식 클래스의 디폴트 대입 연산자는 부모 클래스의 대입 연산자를 호출함
* 자식 클래스의 대입 연산자에서 부모 클래스의 대입 연산자를 직접 호출하지 않으면 부모 클래스의 대입 연산자는 호출되지 않기때문에 명시적으로 호출해줘야함

```c++
class First
{
  private:
  	int n1, n2;
  public:
  	First(int _n1=0, int _n2=0) : n1(_n1), n2(_n2){}
  	First& operator=(const First& ref)
    {
      n1 = ref.n1;
      n2 = ref.n2;
      return *this;
    }
};

class Second : public First
{
  private:
  	int n3, n4;
  public:
  	Second(int _n1, int _n2, int _n3, int _n4) : First(n1, n2), n3(_n3), n4(_n4){}
  	Second& operator=(const Second& ref)
    {
      First::operator=(ref);
      n3 = ref.n3;
      n4 = ref.n4;
      return *this;
    }
}
```

<br/>

#### 배열 인덱스 연산자 오버로딩

* 배열은 경계 검사를 하지 않음
* 배열 클래스는 배열의 역할을 하는 클래스

<br/>

#### 스마트 포인터(Smart Pointer)

<br/>

#### 펑터(Functor)