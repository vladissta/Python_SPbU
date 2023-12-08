import math


def fibonacci(N):
    """
    1. Возвращает N-нй член последовательности Фибоначчи.
    """
    if N < 3:
        return 1  # Первые два члена = 1

    first, second = 1, 1
    for i in range(3, N + 1):
        first, second = second, first + second  # Каждый следующий член - сумма двух предыдущих
    return second


def prime_num(num):
    '''
    2. Проверяет, является ли оно простым.
    '''
    # проверяем делители, начиная с 2 до введенного числа& поделенного попалам,
    # этого достаточно, так как 2 это наименьшее простое число (кроме 1)
    for i in range(2, num // 2):
        if num % i == 0:  # если делится на что-то из данного промежутка – не простое
            return False
    else:
        return True  # иначе - простое


def prime_divisors(num):
    """
    3. Возвращает простые делители введенного числа, или сообщает, что оно простое.
    """
    # проверка простое ли введенное число
    if prime_num(num):
        print(f'{num} is a prime number!')
        return [1, num]

    list_of_prime_divisors = []  # список, в который будем добавлять делители
    # итерируемся до введенного числа под квадратным корнем,
    # этого достаточно, так как максимальный простой делитель может быть только корнем от числа
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            # проверяем оба делителя, так как они оба могут быть простыми
            divisor_1 = num // i
            divisor_2 = num // divisor_1
            # проверка простые ли делители, если да, то добавляем в список:
            if prime_num(divisor_1):
                list_of_prime_divisors.append(divisor_1)
            if prime_num(divisor_2):
                list_of_prime_divisors.append(divisor_2)
    # возвращаем сортированный список
    return sorted(list_of_prime_divisors)


def gcd(num1, num2):
    '''
    4. Находит наибольший общий делитель для двух введенных чисел.
    Реализован Алгоритм Евклида:
    Остаток от деления двух чисел имеет тот же наибольший общий делитель, что и изначальные числа
    '''
    # пока одно из чисел (остаток) не будет равен нулю -
    # это произойдет когда мы найдем НОД
    while num1 != 0 and num2 != 0:
        # заменяем наибольшее число остатком от деления
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return num1 + num2  # (одно из чисел будет равно нулю)


def square_star(n):
    '''
    5.  Запрашивает число, а затем выводит квадрат из *, где длина стороны равна данному числу.
    Список из n звёздочек соединяется в строку, разделенных пробелом звезд, методом join,
    Такие строки соединяются методом join в n строк (разделенные символом \n) - цельный квадрат
    '''
    print("\n".join([' '.join(["*" for _ in range(n)]) for _ in range(n)]))


def rectangle(n, m):
    '''
    6. Запрашивает два числа, а затем выводит прямоугольник из *, где длины сторон равны данным числам.
    Список из n звёздочек соединяется в строку, разделенных пробелом звезд, методом join,
    Такие строки соединяются методом join в m строк (разделенные символом \n) - цельный прямоугольник
    '''
    print("\n".join([' '.join(["*" for _ in range(n)]) for _ in range(m)]))


def snake_num_rectangle(n, m):
    '''
    7. Запрашивает два числа и выводит на экран прямоугольник, в котором змейкой по вертикали записаны числа, начиная с 1.
    Каждая строка - это список из чисел длиной m (начиная с числа 1 + номер строки) с шагом равным n
    Список объединяется в строку методом join (разделенная пробелом)
    Такие строки соединяются методом join в n строк (разделенные символом \n) - цельный прямоугольник-змейку
    '''
    print("\n".join([' '.join([str(i + j + 1) for i in range(0, n * m, n)]) for j in range(n)]))


if __name__ == '__main__':
    print('In last 3 tasks I\'ve just flexed with oneliners :)', end='\n\n')

    print(fibonacci(int(input('Input N: '))))
    print(prime_num(int(input("Input num to check if it's prime: "))))
    print(prime_divisors(int(input("Input num to find its prime divisors: "))))
    print(gcd(*(map(int, input("Input num1 and num2 to find their greatest common divisor: ").split()))))

    square_star(int(input('Input side length to draw square with "*": '))),
    rectangle(*(map(int, input('Input sides lengths to draw rectangle with "*": ').split()))),
    snake_num_rectangle(*(map(int, input('Input sides lengths to draw rectangle with numbers like snake: ').split())))
