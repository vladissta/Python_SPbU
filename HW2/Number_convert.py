import string

digits = string.digits + string.ascii_uppercase  # всевозможные цифры


def convert_to_decimal(num: str, base_in: int) -> int:
    """
    Переводит число из любой системы счисления в десятичную

    :param num: число-строка в любой системе счисления
    :param base_in: система счисления введенного числа
    :return: число в десятичной системе счисления
    """
    decimal_num = 0

    for i, n in enumerate(num):
        decimal_num += digits.index(n.upper()) * (base_in ** (len(num) - i - 1))
    return decimal_num


def convert_from_decimal(num: int, base_out: int) -> str:
    """
    Переводит число из десятичной системы счисления в любую другую

    :param num: число в десятичной системе счисления
    :param base_out: система счисления, в которую надо конвертировать число
    :return: число-строка в новой системе счисления
    """
    out_num_list = []

    while num >= base_out:
        out_num_list.append(digits[num % base_out])
        num //= base_out
    return digits[num] + ''.join(out_num_list[::-1])


def summation(base_in: int, num1: str, num2: str, base_out: int) -> str:
    """
    Числа в одинаковой системе счисления суммируются и переводятся в другую систему счисления
    [!] Вводимые числа - строки, так как есть системы счисления больше чем 10 - там цифры могут быть буквами
    :param base_in: система счисления чисел
    :param num1: Первое число
    :param num2: Второе число
    :param base_out: система счисления, в которой должна быть сумма чисел
    :return: сумма числе в системе счисления base_out
    """
    return convert_from_decimal(convert_to_decimal(num1, base_in) +
                                convert_to_decimal(num2, base_in), base_out)


if __name__ == '__main__':
    assert summation(10, '64', '32', 8) == '140', "10, '64', '32', 8 -> 140 [ERROR]"
    print("10, '64', '32', 8 -> 140 [PASSED]")

    assert summation(2, '10', '10', 8) == '4', "2, '10', '10', 8 -> 4 [ERROR]"
    print("2, '10', '10', 8 -> 4 [PASSED]")

    assert summation(16, 'a', 'a', 10) == '20', "16, 'a', 'a', 10 -> 20 [ERROR]"
    print("16, 'a', 'a', 10 -> 20 [PASSED]")

    assert summation(16, 'a', 'a', 2) == '10100', "16, 'a', 'a', 2 -> 10100 [ERROR]"
    print("16, 'a', 'a', 2 -> 10100 [PASSED]")

    assert summation(2, '101', '110', 16) == 'B', "2, '101', '110', 16 -> 10100 [ERROR]"
    print("2, '101', '110', 16 -> 10100 [PASSED]")

    assert summation(8, '1234', '0', 10) == '668', "8, '1234', '0', 10 -> 668 [ERROR]"
    print("8, '1234', '0', 10 -> 668 [PASSED]")
