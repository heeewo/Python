#set(���� ���� �ڷ���) ���հ� ������ �Լ�
#����� ������ ����.
#�ߺ��Ǵ� ���� �Ѱ��� �����Ѵ�
#��ųʸ��� key�� �����Ѵ�
#����Ʈ�� ����ȵȴ�
#������ &, ������ |, ������ - ���ȴ�
#s.add(a)		���տ� �� ���� ���� �߰��մϴ�.
#s.update([a,b,c...])	���տ� �������� ���� �߰��մϴ�.
#s.remove(a)	���� s�� a�� �����մϴ�.


S1 = {1, 3, 5, 7}
S2 = {5, 6, 7, 8, 9}

print(S1&S2, S1|S2, S1-S2, S2-S1)

S1.add("heeewo")

print(S1)
uplist = ["what", "the", 1, 3]
S2.update(uplist)
print(S2)
S2.remove(9)
print(S2)