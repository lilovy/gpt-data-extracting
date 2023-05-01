from src.tools.multi import thr_bing
from src.tools.extractor import bing_loop
from src.tools.data_loader import load_cookies
from src.tools.proxy import proxy_from_file


proxy_file = "resources\proxies\\bing_proxy.txt"


if __name__ == "__main__":

    cookies = []
    n = 0
    while True:
        n += 1
        try:
            cookies.append(load_cookies(f'./cookies/cookies{n}.json'))
        except Exception as e:
            break

    proxies = proxy_from_file(proxy_file)
    cookie_proxy = [{"cookie": c, "proxy": p} for c, p in list(zip(cookies, proxies))]

    data = (bing_loop, cookie_proxy)

    thr_bing(data=data)
