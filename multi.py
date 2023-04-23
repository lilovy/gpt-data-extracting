import multiprocessing


def multi_process(
    func,
    data: list = load_data(),
    processes: int = 100,
    ):
    print('start parsing!')
    with multiprocessing.Pool(processes=processes) as pool:
        pool.map(func, data)


