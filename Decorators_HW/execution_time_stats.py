import time


class ExecutionStats:
    """
    Tracks execution stats for a function.
    """

    def __init__(self, func):
        self.func = func
        self.execution_times = []

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        result = self.func(*args, **kwargs)
        end_time = time.perf_counter()

        curr_execution_time = end_time - start_time
        self.execution_times.append(curr_execution_time)

        print(f"\033[92m-{'-'*25}\033[0m")
        print(f"Current execution time: \033[94m{curr_execution_time:.4f} seconds\033[0m")
        print(f"Mean execution time: \033[96m{sum(self.execution_times) / len(self.execution_times):.4f} seconds\033[0m")
        print(f"Min execution time: \033[96m{min(self.execution_times):.4f} seconds\033[0m")
        print(f"Max execution time: \033[96m{max(self.execution_times):.4f} seconds\033[0m")

        return result


@ExecutionStats
def my_function(sleep_time):
    time.sleep(sleep_time)


if __name__ == '__main__':
    my_function(1)
    my_function(2)
    my_function(1)
