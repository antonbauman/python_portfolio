while True:

    number = int(input('Ведіть індекс числа Фібоначі: '))

    if number == 666:
        print('Програму зупинено')
        break

    def gen_fib(number):
        f1, f2 = 0, 1
        for item in range(number):
            yield f2
            f1, f2 = f2, f1 + f2

    generator = list(gen_fib(number))
    print(generator[-1])

    # print(type(gen_fib(number)))
