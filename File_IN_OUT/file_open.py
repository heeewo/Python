#프로그램은 서버의 파일에 회원정보가 담기고 프로그램이 서버의 파일을 읽어보고 사용자의 정보 입력과 대조하여 결과를 출력하는것
#tip map() >> map(함수,값의집합인자1,값의집합인자2...) 값의 집합인자는 튜플,리스트,문자열 함수의 기능을 수행할때 사용 즉 집합에 함수를 다돌릴때 씀 list형식변환해야함!!
#파일 생성/열기 파일 객체 이름 = open("파일경로/파일이름","파일열기모드")형식
#*******파일을 열고 썻다면 바드시 닫아줘야한다 파일객체.close()형식으로
#r  읽기모드 - 파일을 읽기만 할때 사용
#w  쓰기모드 - 파일에 내용을 새로 쓸 때 사용
#a  추가모드 - 파일의 마지막 부분에 새로운 내용을 추가할 때 사용
#파일을 쓸때는 파일객체.write(인자) 여기서 인자는 문자열만 된다.리스트 등등다됨
#구름 IDE에서는 data라는 파일 결로를 제공하기때문에 거기서 실행하면됨

A = [1,7,6,3]
A = sorted(A)
F = open("out.txt",'w')
F.write(str(A))
F.close()  

a = open('out.txt','r')
b = a.read()
print(b)
a.close()
