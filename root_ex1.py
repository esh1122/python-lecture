def root_ex(a,b,c):
    x_1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x_2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

    return x_1 , x_2

a = int(input('2차항의 계수 : '))
b = int(input('1차항의 계수 : '))
c = int(input('상수항 : '))

root_ex(a,b,c)
print(f'해는 {x_1} 또는 {x_2}')