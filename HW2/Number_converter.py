import string

# Список перевода чисел от 0 до 15 в буквенные значения
d_16 = dict(
    zip(
        string.hexdigits, list(range(16))
    )
)


def int_copy(num_list: list[str] | str) -> int:
    """
    Небольшая копия функции int()
    :param num_list: список или строка ЦИФР
    :return: Число, с конкатинированными цифрами из списка
    """
    num_out = 0
    for p, num in enumerate(num_list[::-1]):
        num_out += d_16[num.lower()] * (10 ** p)
    return num_out


def decimal_to_any(decimal_in: str, base_out: int) -> int:
    """
    Переводит число из десятичной системы счисления в любую другую
    :param decimal_in: число-строка в десятичной системе счисления
    :param base_out: система счисления, в которую надо конвертировать число
    :return: число в новой системе счисления
    """
    stack = []
    decimal_int = int_copy(decimal_in)

    stack.append(str(decimal_int % base_out))
    decimal_int //= base_out

    while decimal_int:
        stack.append(str(decimal_int % base_out))
        decimal_int //= base_out

    stack.reverse()
    return int_copy(stack)


def any_to_decimal(num_in: str, base_in: int) -> list:
    """
    Переводит число из любой системы счисления в десятичную
    :param base_in: система счисления введенного числа
    :param num_in: число-строка в любой системе счисления
    :return: список из строк-чисел в десятичной системе счисления
    """
    num_out = 0
    for n, num in enumerate(list(num_in)[::-1]):
        num_out += d_16[num] * (base_in ** n)

    return list(str(num_out))


def convert_number(base_in, num1: str, num2: str, base_out) -> tuple[int, int]:
    """
    Конвертирует числа в нужную систему счисления
    :param base_in: система счисления чисел
    :param num1: Первое число
    :param num2: Второе число
    :param base_out: выходная система счисления
    :return: кортеж из двух чисел в нужной системе счисления
    """
    if base_in != 10:
        num1 = any_to_decimal(num1, base_in)
        num2 = any_to_decimal(num2, base_in)

    if base_out == 10:
        return int_copy(num1), int_copy(num2)

    return decimal_to_any(num1, base_out), decimal_to_any(num2, base_out)


def summation(base_in: int, num1: str, num2: str, base_out: int):
    """
    Числа в одинаковой системе счисления суммируются и переводятся в другую систему счисления
    [!] Вводимые числа - строки, так как есть системы счисления больше чем 10 - там цифры могут быть буквами
    :param base_in: система счисления чисел
    :param num1: Первое число
    :param num2: Второе число
    :param base_out: система счисления, в которой должна быть сумма чисел
    :return: сумма числе в системе счисления base_out
    """
    num1, num2 = convert_number(base_in, num1, num2, base_out)
    num_list = []
    in_mind = 0

    while num1 + num2 != 0:
        s1 = num1 % 10 + num2 % 10 + in_mind
        num_list.append(str(s1 % base_out))
        in_mind = s1 // base_out

        num1 //= 10
        num2 //= 10

    num_list.append(str(in_mind))
    num_list.reverse()

    return int_copy(num_list)


if __name__ == '__main__':
    assert summation(10, '64', '32', 8) == 140
    print("10, '64', '32', 8 -> 140 [PASSED]")

    assert summation(2, '10', '10', 8) == 4, "2, '10', '10', 8 -> 4 [ERROR]"
    print("2, '10', '10', 8 -> 4 [PASSED]")

    assert summation(16, 'a', 'a', 10) == 20, "16, 'a', 'a', 10 -> 20 [ERROR]"
    print("16, 'a', 'a', 10 -> 20 [PASSED]")

    assert summation(16, 'a', 'a', 2) == 10100, "16, 'a', 'a', 2 -> 10100 [ERROR]"
    print("16, 'a', 'a', 2 -> 10100 [PASSED]")

    assert summation(8, '1234', '0', 10) == 668, "8, '1234', '0', 10 -> 668 [ERROR]"
    print("8, '1234', '0', 10 -> 668 [PASSED]")
