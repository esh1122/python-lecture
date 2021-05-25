selected = None
while selected not in ['바위']:
    selected = input('가위, 바위, 보 중에서 선택하세요> ')
    print('선택한 값은:', selected)
    if (selected == '바위') :
        print('You win')