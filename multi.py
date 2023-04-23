import multiprocessing


def multi_process(
    func,
    data: list,
    processes: int = 2,
    ):
    print('start parsing!')
    with multiprocessing.Pool(processes=processes) as pool:
        pool.map(func, data)


