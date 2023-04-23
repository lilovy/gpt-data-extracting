import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time:.5f} секунд")
        return result
    return wrapper

# def timer(func):
    # def wrapper(*args, **kwargs):
    #     start_time = time.time()
    #     elapsed_time = 0
    #     while True:
    #         result = func(*args, **kwargs)
    #         elapsed_time = time.time() - start_time
    #         print(f"Прошло {elapsed_time:.5f} секунд")
    #         time.sleep(1)  # приостанавливаем выполнение программы на 1 секунду
    #         if elapsed_time >= 1:  # если прошло более 1 секунды, прерываем цикл и выводим общее время выполнения функции
    #             break
    #     print(f"Время выполнения функции {func.__name__}: {elapsed_time:.5f} секунд")
    #     return result
    # return wrapper