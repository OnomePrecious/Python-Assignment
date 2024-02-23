from time import time


#    def decorate

def time_taken(func):
    def wrap(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"it took {t2 - t1:.3f} ms to execute")
        return result

    return wrap


@time_taken
def get_list(numbers):
    result = []
    for i in range(numbers):
        result.append(i)
        return result

    get_list(1000000)
