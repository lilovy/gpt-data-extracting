from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as mp



def multi_process(
    func,
    tokens: list,
    processes: int = 2,
    ):
    print('start parsing!')
    with mp.Pool(processes=processes) as pool:
        pool.map(func, tokens)


def mlt(
    func,
    data,
):
    processes = []
    for t, proxy in data:
        p = mp.Process(target=func, args=(t, proxy,))
        processes.append(p)
        p.start()
    
    # for p in processes:

    for p in processes:
        p.join()