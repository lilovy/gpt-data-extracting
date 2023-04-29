from src.tools.multi import thr_bing
from src.tools.extractor import start_bing, bing_loop
from config import proxies
from src.tools.data_loader import load_cookies


if __name__ == "__main__":

    cookie = load_cookies('./cookies/cookies1.json')
    proxy = proxies[-1]

    data = (bing_loop, [{"cookie": cookie, "proxy": proxy}])

    thr_bing(data=data)
