def sum_nums(*args) :
    n = len(args)
    s = 0
    print(f'{n} 개의 인자 {args}')
    for arg in args :
        s += arg
    print(f'합계 : {s} , 평균 : {s/n}')

sum_nums(10,20,30)
sum_nums(10,20,30,40,50)