def fibbonacci(n):
    """
    Recursive calculation of n-th number in Fibonacci sequence starting with 0 element (!)
    :param n: number
    :return: n-th number in Fibonacci sequence
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibbonacci(n - 1) + fibbonacci(n - 2)


if __name__ == '__main__':
    assert fibbonacci(1) == 1, '[TEST 1 FAILED]'
    print('TEST 1 PASSED')
    assert fibbonacci(5) == 5, '[TEST 2 FAILED]'
    print('TEST 2 PASSED')
    assert fibbonacci(10) == 55, '[TEST 3 FAILED]'
    print('TEST 3 PASSED')
    assert fibbonacci(20) == 6765, '[TEST 4 FAILED]'
    print('TEST 4 PASSED')
    print('Everything is kay')
