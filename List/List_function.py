#append(x)	리스트 맨 마지막에 전달 인자를 추가합니다.
#remove(x)	리스트에서 가장 처음 나오는 x 값을 삭제합니다.
#insert(x,y)	리스트의 x 번째 위치에 y 값을 추가합니다.
#pop()		리스트의 마지막 요소를 반환한 뒤 리스트에서 삭제합니다.
#extend(x)	기존 리스트에 x를 합칩니다. 전달인자에는 리스트만 입력가능합니다.
#sort()		리스트의 요소를 순서대로 정렬합니다. 전달 인자가 필요없는 함수
#reverse()	리스트의 순서를 반대로 뒤집습니다. 전달 인자가 필요 없는 함수
#index(x)		전달 인자가 리스트 안에 있으면 해당 요소의 인덱스 값을 반환합니다.
#count(x)		리스트에 있는 x값의 개수를 반환합니다.
#len(list)		리스트의 길이를 반환합니다.
#리스트는 서랍장과 같다 칸을 만들어주고 넣어야한다 칸이 없는경우 append 여러개는 extend를 사용한다
#리스트[?] = ""는 빈칸을 만들지만 칸을 삭제하는게 아니다 remove를 써야한다

a = [1, 9, 2, 3, 4, 5, 7]
a.sort()

print(a)
a.remove(9)
print(a)
a.insert(5, 6)
print(a)
a.append(8)
print(a)
a.reverse()
print(a)
