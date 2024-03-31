import time
import datetime
import logging
from functools import wraps


def log_execution_time(func):
    """
    Logs the time it takes for a function to execute.
    """

    @wraps(func)
    def inner_function(*args, **kwargs):
        start_time = time.perf_counter()
        print(f'Starting execution of {func.__name__}: at {datetime.datetime.now():%Y-%m-%d %H:%M:%S}')
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'Finished execution of {func.__name__} in {end_time - start_time:.4f} seconds at \
{datetime.datetime.now():%Y-%m-%d %H:%M:%S}')

        return result

    return inner_function


@log_execution_time
def my_function(sleep_time):
    time.sleep(sleep_time)


if __name__ == '__main__':
    my_function(1)
