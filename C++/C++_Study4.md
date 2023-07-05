[템플릿](#템플릿template)

[함수 템플릿](#함수-템플릿)

[클래스 템플릿](#클래스-템플릿)

[형 변환 연산자](#형-변환-연산자)

<br/>

#### 템플릿(Template)

* ​

<br/>

#### 함수 템플릿

* 기능만 정의하고 여러 자료형의 함수를 만들 수 있는 틀
* 컴파일러가 함수의 호출 문장을 보고 해당 자료형의 형태로 함수를 만듦(자료형당 하나씩만 만듦)
* 컴파일 시 함수가 만들어지기 때문에 속도가 느릴 수 있지만 컴파일 속도가 느린 것이지 실행 속도가 느린 것은 아님
* 함수 템플릿을 기반으로 컴파일러가 만드는 함수들을 템플릿 함수

```c++
template <typename T>
T Add(T n1, T n2)
{
  return n1 + n2;
}

template <typename T1, typename T2>
void Show(int num)
{
  cout<<(T1)num<<endl;
  cout<<(T2)num<<endl;
}

int main()
{
  cout<<Add<int>(15, 20)<<endl;
  cout<<Add<double>(2.1, 3.9)<<endl;
  cout<<Add<int>(3.1, 3.9)<<endl;   // 7이 출력됨, T가 int형인 함수를 호출했기 때문
  
  // 전달되는 인자의 자료형을 참조해 컴파일러가 호출할 함수를 구분하므로 자료형 지정 안해도 됨
  cout<<Add(15, 20)<<endl;
  cout<<Add(2.1, 3.9)<<endl;
  cout<<Add(3.1, 3.9)<<endl;
  
  Show<char, int>(65);   // A와 65 출력됨
  Show<char, int>(67);   // C와 67 출력됨
}
```

* 함수 템플릿의 특수화(Specializtion of Function Template)
* * 상황에 따라 템플릿 함수의 구성 방법에 예외가 필요할 수 있음
  * 문자열을 비교할 때 길이 비교가 목적인지, 사전편찬 순서 비교가 목적인지

```c++
template <typename T>
T Max(T a, T, b)
{
  return a > b ? a : b;
}

template <>   // 특수화
char* Max(char *a, char *b)
{
  return strlen(a) > strlen(b) ? a : b;   // 길이 비교
}

template <>  // 특수화
const char* Max(const char *a, const char *b)
{
  return strcmp(a, b) > 0 ? a : b;   // 사전편찬 순서 비교
}

int main()
{
  cout<<Max(11, 15)<<endl;
  cout<<Max(5.5, 3.3)<<endl;
  cout<<Max("Simple", "Complex")<<endl;   
  // 문자열 선언으로 인해 반환되는 주소 값의 포인터 형이 const char*이므로 const char* Max형에 대해 특수화된 함수가 호출
  
  char str1[] = "Simple";
  char str2[] = "Complex";
  cout<<Max(str1, str2)<<endl;
  // str1과 str2가 변수 형태로 선언되어 포인터 형이 char*이므로 char* Max형에 대해 특수화된 함수가 호출
}
```

<br/>

#### 클래스 템플릿

* 클래스를 템플릿으로 정의한 것이 클래스 템플릿
* 클래스 템플릿을 기반으로 컴파일러가 만든 클래스가 템플릿 클래스
* 클래스 템플릿을 기반으로 객체를 생성할 때는 자료형을 명시해야함

```c++
template <typename T>
class Point
{
  private:
  	T xpos, ypos;
  public:
  	Point(T x=0, T y=0) : xpos(x), ypos(y){}
  	void Show()
    {
      cout<<xpos<<"   "<<ypos<<endl;
    }
};

int main()
{
  Point<int> pos1(3, 4);
  pos1.Show();
  
  Point<double> pos2(3.3, 4.4);
  pos2.Show();
  
  Point<char> pos3('P', 'F');
  pos3.Show();
}
```

```c++
template <typename T>
class Point
{
  private:
  	T xpos, ypos;
  public:
  	Point(T x=0, T y=0) : xpos(x), ypos(y){}
};

template <typename T>
class BoundCheckArr
{
  private:
  	T *arr;
  	int arrLen;
};

int main()
{
  // 클래스 템플릿을 기반으로 객체를 생성하는 규칙
  BoundCheckArr<Point<int>> arr1(10);
  BoundCheckArr<Point<int>*> arr2(20);
}
```

* 클래스 템플릿의 특수화(Specilization of Class Template)
* * 특정 자료형을 기반으로 생성된 객체에 대해 다른 양식을 적용하기 위함

```c++
template <typename T>
class Simple
{
  private:
  	T data;
  public:
  	Simple(T _data) : data(_data){}
  	void Show(){cout<<data<<endl;}
};

template <typename T>
class Simple < char*>
{
  private:
  	char *data;
  public:
  	Simple(char *_data)
    {
    	data = new char[strlen(_data) + 1];
    	strcpy(data, _data);
    }
    void Show()
    {
    	cout<<data<<endl;
    	cout<<strlen(data)<<endl;
    }
    ~Simple()
    {
    	delete []data;
    }
};

int main()
{
  Simple<int> s1(10);
  s1.Show();
  
  Simple<char*> s2("Class Template Specialization");
  s2.Show();
}
```

<br/>

#### 형 변환 연산자



