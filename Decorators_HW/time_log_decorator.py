import time
import datetime
import logging


def log_execution_time(func):
    """
    Logs the time it takes for a function to execute.
    """

    logging.basicConfig(level=logging.INFO, filename=func.__name__ + '.log')

    def inner_function(*args, **kwargs):
        start_time = time.perf_counter()
        logging.info(f'Starting execution of {func.__name__}: at {datetime.datetime.now():%Y-%m-%d %H:%M:%S}')
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        logging.info(f'Finished execution of {func.__name__} in {end_time - start_time:.4f} seconds at \
{datetime.datetime.now():%Y-%m-%d %H:%M:%S}')

        return result

    return inner_function


@log_execution_time
def my_function(sleep_time):
    time.sleep(sleep_time)


if __name__ == '__main__':
    my_function(1)
