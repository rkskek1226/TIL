[복사 생성자](#복사-생성자)

[static 멤버 변수(클래스 변수)](#static-멤버-변수)

[static 멤버 함수](#static-멤버-함수)

[mutable](#mutable)

[상속](#상속)

[상속을 위한 조건](#상속을-위한-조건)

[객체 포인터](#객체-포인터)

[가상 함수](#가상-함수virtual-function)

[추상 클래스](#추상-클래스)

[가상 소멸자](#가상-소멸자)

[가상 함수 테이블](#가상-함수-테이블)

[다중 상속](#다중-상속)

<br/>

#### 복사 생성자

* 자신과 같은 클래스 타입의 객체에 대한 참조를 인자로 받아 해당 참조를 가지고 자신을 초기화하는 생성자
* 복사 생성자를 정의하지 않으면 디폴트 복사 생성자가 호출되고 디폴트 복사 생성자는 얕은 복사를 수행
* 깊은 복사를 위해 복사 생성자를 정의하는 것이 좋음

```c++
class Simple
{
  private:
  	int num1, num2;
  public:
  	Simple(int n1, int n2) : num1(n1), num2(n2){}
  	Simple(const Simple &copy) : num1(copy.num1), num2(copy.num2){}   // 복사 생성자
};
```

<br/>

#### static 멤버 변수

* 클래스 내에서 사용되는 static 멤버 변수는 클래스 변수라고도 함
* 객체가 생성될 때마다 함께 생성되어 객체별로 존재하는 변수가 아닌 하나만 할당되어 공유되는 변수
* static 멤버 변수는 생성자에서 초기화하면 안됨(생성자에서 초기화하면 객체가 생성될 때마다 해당 값으로 초기화되므로 별도로 정의해야함)
* public으로 선언되면 클래스의 이름을 통해 어디서든 접근이 가능(Simple::cnt;)

```c++
class Simple:
{
  private:
  	static int cnt;
  public:
  	Simple()
    {
      cnt++;
      cout<<cnt<<"번째 객체"<<endl;
    }
  	Simple(Simple &copy)
    {
      cnt++;
      cout<<cnt<<"번째 객체"<<endl;
    }
};
int Simple::cnt = 0;   // static 멤버 변수 초기화
```

<br/>

#### static 멤버 함수

* 선언된 클래스의 모든 객체가 공유하고 public으로 선언되면 클래스의 이름을 통해 호출이 가능
* 객체의 멤버로 존재하는 것이 아님
* static 멤버 함수에서는 static 멤버 변수만 호출 가능

```c++
class Simple
{
  private:
  	int n1;
  	static int n2;
  public:
  	Simple(int n1) : n1(n1){}
  	static void Adder(int n)
    {
      n1 += n;   // 컴파일 에러 발생
      n2 += n;
    }
};
// 컴파일 에러 발생 이유
// 1. 객체의 멤버가 아니므로 멤버 변수에 접근할 수 없음
// 2. 만약 접근한다고 가정해도 어떤 객체의 멤버 변수인지도 알 수 없음
```

<br/>

#### mutable

* const 함수 내에서 값의 변경을 예외적으로 허용한다는 의미

<br/>

#### 상속

* 연관된 일련의 클래스에 대해 공통적인 규약을 정의할 수 있음


* 부모 클래스의 속성을 자식 클래스가 물려받는 것
* 자식 클래스의 객체 생성 과정에서 자식 클래스의 생성자가 부모 클래스의 생성자 호출을 명시하지 않는다면 부모 클래스의 void 생성자가 호출됨
* 자식 클래스의 객체가 소멸될 때는 자식 클래스의 소멸자가 실행된 후 부모 클래스의 소멸자가 실행됨

```c++
class Base
{
  private:
  	int baseNum;
  public:
  	Base() : baseNum(20){}
  	Base(int n) : baseNum(n){}
  	void ShowBaseNum(){cout<<baseNum<<endl;}
};

class Derived : public Base
{
  private:
  	int derivNum;
  public:
  	Derived() : derivNum(30){}
  	Derived(int n) : derivNum(n){}
  	Derived(int n1, int n2) : Base(n1), derivNum(n2){}
  	void ShowDerivNum()
    {
    	ShowBaseNum();
    	cout<<derivNum<<endl;
    }
};

int main()
{
  Derived dr1;   // 부모 클래스의 void 생성자도 호출됨
  Derived dr2(12);   // 부모 클래스의 void 생성자도 호출됨
  Derived dr3(23, 24);
}
```

* 상속의 유형

* * protected 상속
  * * protected보다 접근 범위가 넓은 멤버는 protected로 변경시켜서 상속 받음
  * private 상속
  * * private보다 접근 범위가 넓은 멤버는 private으로 변경시켜서 상속 받음
  * public 상속
  * * public보다 접근 범위가 넓은 멤버는 public으로 변경시켜서 상속 받음
    * private을 제외한 나머지는 그대로 상속

  ```c++
  class Base
  {
    private:
    	int n1;
    protected:
    	int n2;
    public:
    	int n3;
  };

  clsss ProtectedDerived : protected Base
  {
    // n1에는 접근 불가(Base에서 n1이 private이므로)
    // n2와 n3은 protected
  };

  class PrivateDerived : private Base
  {
    // n1에는 접근 불가(Base에서 n1이 private이므로)
    // n2와 n3은 private
  };

  class PublicDerived : public Base
  {
    // n1에는 접근 불가(Base에서 n1이 private이므로)
    // n2는 protected, n3은 public
  };
  ```


<br/>

#### 상속을 위한 조건

* IS-A 관계
* * AA is a BB
  * 전화기와 무선 전화기가 있을 때 무선 전화기 is a 전화기
  * 컴퓨터와 노트북이 있을 때 노트북 is a 컴퓨터
* HAS-A 관계
* * AA has a BB
  * 경찰과 권총이 있을 때 경찰 has a 권총
  * 사실 HAS-A 관계는 상속이 아닌 다른 방식으로 표현이 가능
  * 만약 권총을 소유하지 않은 경찰을 표현해야 하거나 경찰이 다른 무기도 소유할 경우 변경하기 힘들어지거나 다중 상속을 해야함
  * 그러므로 상속으로 표현하기보단 멤버 변수로 추가하는 것이 좋음

<br/>

#### 객체 포인터

* 객체 포인터 변수는 객체의 주소 값을 저장하는 포인터 변수
* OO형 포인터 변수는 OO형 객체나 OO형 객체를 상속받는 객체를 가리킬 수 있음
* C++ 컴파일러는 포인터 연산의 가능성을 판단할 때 포인터의 자료형을 기반으로 하며 실제 가리키는 객체의 자료형을 기준으로 판단하지 않음
* 포인터 형에 해당하는 클래스에 정의된 멤버 함수에만 접근이 가능

```c++
class Base()
{
  public:
  	void BaseFun(){cout<<"Base Func"<<endl;}
};

class Derived : public Base
{
  public:
  	void Derived(){cout<<"Derived Func"<<endl;}
};

int main()
{
  Base *ptr1 = new Base();   // ptr1은 Base 객채의 주소를 가리킴
  Base *ptr2 = new Derived();   // ptr2는 Derived 객체의 주소를 가리킴
  ptr2->Derived();   // 컴파일 에러, ptr2가 Base형 포인터이고 이를 기반으로 하기때문
  Derived *ptr3 = ptr2;   // 컴파일 에러, 컴파일러는 ptr2가 가리키는 객체가 Derived라는 사실을 기억하지 않음, ptr2가 Base형 포인터라는 사실만 기억함
  Derived *ptr4 = new Derived();
  Base *ptr5 = ptr4;   // 컴파일 성공, ptr4는 Derived형이고 Derived가 Base를 상속받기때문
}
```

```c++
class First
{
  public:
  	void FirstFunc(){cout<<"First Func"<<endl;}
  	void MyFunc(){cout<<"First MyFunc"<<endl;}
};

class Second : public First
{
  public:
  	void SecondFunc(){cout<<"Second Func"<<endl;}
  	void MyFunc(){cout<<"Second MyFunc"<<endl;}
};

class Third : public Second
{
  public:
  	void ThirdFunc(){cout<<"Third Func"<<endl;}
  	void MyFunc(){cout<<"Third MyFunc"<<endl;}
};

int main()
{
  Third *tptr = new Third();   // 컴파일 성공
  Second *sptr = tptr;   // 컴파일 성공
  First *fptr = sptr;   // 컴파일 성공
  
  tptr->FirstFunc();   // 컴파일 성공
  tptr->SecondFunc();   // 컴파일 성공
  tptr->ThirdFunc();   // 컴파일 성공
  
  sptr->FirstFunc();   // 컴파일 성공
  sptr->SecondFunc();   // 컴파일 성공
  sptr->ThirdFunc();   // 컴파일 실패
  
  fptr->FirstFunc();   // 컴파일 성공
  fptr->SecondFunc();   // 컴파일 실패
  fptr->ThirdFunc();   // 컴파일 실패
  
  fptr->MyFunc();   // First MyFunc 출력
  sptr->MyFunc();   // Second MyFunc 출력
  tptr->MyFunc();   // Third MyFunc 출력
}
```

<br/>

#### 가상 함수(Virtual Function)

* virtual 키워드를 사용해 가상 함수로 선언하고 해당 가상 함수를 오버라이딩하는 함수도 가상 함수가 됨
* 자식 클래스에서 재정의할 것으로 기대하고 기존에 정의한 내용들이 새롭게 정의한 내용들로 대체되는 것으로 동적 바인딩을 위한 함수

```c++
class First
{
  public:
  	virtual void MyFunc(){cout<<"First MyFunc"<<endl;}
};

class Second : public First
{
  public:
  	virtual void MyFunc(){cout<<"Second MyFunc"<<endl;}   // virtual 키워드 안 써도 되지만 작성해주는 것이 좋음
};

class Third : public Second
{
  public:
    virtual void MyFunc(){cout<<"Third MyFunc"<<endl;}   // virtual 키워드 안 써도 되지만 작성해주는 것이 좋음
}

int main()
{
  Third *tptr = new Third();
  Second *sptr = tptr;
  First *fptr = sptr;
  
  fptr->MyFunc();   // Third MyFunc 출력
  sptr->MyFunc();   // Third MyFunc 출력
  tptr->MyFunc();   // Third MyFunc 출력
}
```

<br/>

#### 추상 클래스

* 기초 클래스로서만의 의미를 가져 순수 가상 함수를 가지는 객체 생성을 목적으로 하지 않는 클래스
* 추상 클래스를 대상으로 객체를 생성하려한다면 아마도 개발자의 실수이겠지만 컴파일러는 에러를 발생시키지 않음
* 가상 함수를 순수 가상 함수로 선언해 해결할 수 있음
* 순수 가상 함수는 함수의 몸체가 정의되지 않은 함수로 0을 대입해 표시

```c++
class Base
{
  private:
  	int num;
  public:
  	virtual int GetNum() = 0;
}
```

<br/>

#### 가상 소멸자

* virtual로 선언된 소멸자
* 상속 관계에서 부모 클래스의 소멸자를 virtual로 선언하면 자식 클래스의 소멸자들도 가상 소멸자로 선언됨
* 가상 소멸자가 호출되면 자식 클래스의 소멸자가 호출되는데 기초 클래스의 소멸자들이 순차적으로 먼저 호출됨

```c++
class First
{
  private:
  	char* one;
  public:
  	First(char *str)
    {
      one = new char[strlen(str) + 1];
    }
  	~First()
    {
      delete []one;
    }
  	/*
  	virtual ~First()
    {
      delete []one;
    }
    */
};

class Second : public First
{
  private:
    char *two;
  public:
  	Second(char *str1, char *str2) : First(str1)
    {
    	two = new char[strlen(str2) + 1];
    }
    ~Second()
    {
    	delete []two;
    }
};

int main()
{
  First *ptr = new Second("simple", "complex");
  delete ptr;   // First 소멸자만 호출되고 Second의 소멸자는 호출되지 않음 
}
```

<br/>

#### 가상 함수 테이블

<br/>

#### 다중 상속



