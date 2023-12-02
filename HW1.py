import math


def fibonacci(N):
    """
    1. Возвращает N-ный член последовательности Фибоначчи.
    Числа Фиббоначи: первые два члена 1 и 1.
    Каждый следующий член - сумма двух предыдущих.
    """
    first, second = 1, 1
    if N < 3:
        return 1
    else:
        for i in range(3, N + 1):
            first, second = second, first + second
    return second


def prime_num(num):
    '''
    2. Проверяет, является ли оно простым.
    '''
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    else:
        return True


def prime_divisors(num):
    """
    3. Возвращает простые делители введенного числа, или сообщает, что оно простое.
    """
    list_of_prime_divisors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor_1 = num // i
            divisor_2 = num // divisor_1
            if prime_num(divisor_1):
                list_of_prime_divisors.append(divisor_1)
            if prime_num(divisor_2):
                list_of_prime_divisors.append(divisor_2)

    return list_of_prime_divisors


def gcd(num1, num2):
    '''
    4. Находит наибольший общий делитель для двух введенных чисел.
    '''
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return num1 + num2


def square_star(n):
    '''
    5.  Запрашивает число, а затем выводит квадрат из *, где длина стороны равна данному числу.
    '''
    print("\n".join([' '.join(["*" for _ in range(n)]) for _ in range(n)]))


def rectangle(n, m):
    '''
    6. Запрашивает два числа, а затем выводит прямоугольник из *, где длины сторон равны данным числам.
    '''
    print("\n".join([' '.join(["*" for _ in range(n)]) for _ in range(m)]))


def snake_num_rectangle(m, n):
    '''
    7. Запрашивает два числа и выводит на экран прямоугольник, в котором змейкой по вертикали записаны числа, начиная с 1.
    '''
    print("\n".join([' '.join([str(i + j + 1) for i in range(0, n * m, m)]) for j in range(m)]))


if __name__ == '__main__':
    print('In last 3 tasks I\'ve just flexed with oneliners :)', end='\n\n')

    print(fibonacci(int(input('Input N: '))))
    print(prime_num(int(input("Input num to check if it's prime: "))))
    print(prime_divisors(int(input("Input num to find its prime divisors: "))))
    print(gcd(*(map(int, input("Input num1 and num2 to find their greatest common divisor: ").split()))))

    square_star(int(input('Input side length to draw square with "*": '))),
    rectangle(*(map(int, input('Input sides lengths to draw rectangle with "*": ').split()))),
    snake_num_rectangle(*(map(int, input('Input sides lengths to draw rectangle with numbers like snake: ').split())))
