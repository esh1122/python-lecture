a = int(input("a를 입력하세요!"))
b = int(input("b를 입력하세요!"))
if (a % 2 == 0) and (b % 2 == 0) :
    print('두 수 모두 짝수')
if (a % 2 == 0) or (b % 2 == 0) :
    print('두 수 중 하나는 짝수')