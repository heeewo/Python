#count()		���� ������ ���� ������ ��ȯ
#find()		�Լ��� ����� �Ǵ� ���ڿ��� ���� ���ڿ� ���� ���ڰ� �ִ��� ã�� �׹��ڰ� ó�� �߰ߵ� �ε��� ���� ��ȯ. ���� �������ڰ� ���ڿ� ���� ���ٸ� -1 ��ȯ
#index()		���ε�� ���� ��Ȱ, ���� ���ڰ� ���ڿ� ���� ������ ���� �߻�
#join()		���� ���� ���̿� �Լ��� ����� �Ǵ� ���ڿ��� ����
#upper() /lower()	�Լ��� ����� �Ǵ� ���ڿ��� �빮�ڷ� / �ҹ��ڷ� ��ȯ
#lstrip() /rstrip()	�Լ��� ����� �Ǵ� ���ڿ��� ���� ����/������ ������ ��� ����
#strip()		�Լ��� ����� �Ǵ� ���ڿ��� �� �ʿ� �ִ� �� ĭ �̻��� ���� ��� ����
#replace()	replace(��������1, ��������2) ���Ĥ��� ����ϸ�,�Լ��� ����� �Ǵ� ���ڿ����� ��������1�� ������ �κ��� ã�� ��������2�� �ٲ�
#split()		�Լ��� ����� �Ǵ� ���ڿ��� �������� �������� �ɰ� ����Ʈ�� ��ȯ(ex. "g!oo!rm".split("!") > ['g','oo','rm']
#len()		���ڿ� ����
a = "Contrary to popular belief, Lorem Ipsum is not simply random text."

print(a.count('t'))

print(a.index('i'))

print(a.upper())

print(a.lower())

print(a.replace('a', 'b'))

print(a.split(" "))