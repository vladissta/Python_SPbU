def n_times_executor(n: int):
    def decorator(func):
        def inner_function(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return inner_function

    return decorator


@n_times_executor(4)
def print_test():
    print('test')


if __name__ == '__main__':
    print_test()
