from src.tools.multi import multi_process, mlt, thr, thr_bing
from src.tools.extractor import combine, api_combine, start_bing
from config import tokens, tok_prx, proxies, api_prx
from src.tools.data_loader import load_cookies



n = 0

if __name__ == "__main__":
    # multi_process(combine, tok_prx, processes=len(tok_prx))
    # mlt(combine, tok_prx)
    # mlt(api_combine, api_prx)
    cookie = load_cookies('./cookies/cookies2.json')
    proxy = proxies[0]

    # cookie_prx = list(zip(cookie, proxies))
    # print(cookie_prx)
    
    # data = [(combine, tok_prx)]
    data = (start_bing, [{"cookie": cookie, "proxy": proxy}])
    # print(data)
    # thr(data)
    thr_bing(data=data)
    # combine(tokens[n], proxies[n])