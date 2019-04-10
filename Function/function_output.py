#매개변수
#함수는 크게 매개변수, 기능(실행구문), 반환값으로 이루어져 있다
#매개변수가 2개로 설정하면 전달인자도 2개가 된다
#매개변수를 지정해서 전달할수도 있다 ex) def subNums(a, b) :  >>> subNums(b = 10,a =3) 했을시 subNums(3,10) 으로 인식한다
#다만 매개변수 지정시 하나만 지정하고 변수를 넣으면 에러가뜬다
#매개변수는 무한히 넣을수있다'가변인자함수' : "def 함수이름(*매개변수):"식이며 가변인자는 튜플로 저장
#일반 매개변수와 가변인자함수를 같이 쓸수있으나 가변인자 함수가 뒤로와야한다 왜냐하면 가변인자함수가 먼저오면 일반매개변수도 가변인자로 인식
#'키워드 매개변수' : "def 함수이름(**매개변수):"식이며 읻셔너리 형태로 선언가능
#다만 키(key)는 따옴표를 감싸지 않고 변수처럼 입력해야한다
#키워드 매개변수와 가변인자를 같이 사용할수있는데키워드매개변수 뒤에 키워드매개변수가 아닌것이 올수 없음으로 (일반매개변수, 가변인자함수,키워드매개변수)순으로 입력

def my_func(str) :
	a = str.upper()
	b = str.lower()
	return a, b

print(my_func("Hello World!"))
