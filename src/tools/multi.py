import multiprocessing as mp


def multi_process(
    func,
    tokens: list,
    processes: int = 2,
    ):
    print('start parsing!')
    with mp.Pool(processes=processes) as pool:
        pool.map(func, tokens)


