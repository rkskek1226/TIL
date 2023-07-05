qwewqewq

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

