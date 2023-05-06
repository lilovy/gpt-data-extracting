# from src.tools.multi import thr_bing
from src.tools.extractor import bing_loop
from src.tools.data_loader import load_cookies
from src.tools.proxy import proxy_from_file
from src.database.init_database import DB
import threading as tr


proxy_file = "resources\proxies\\bing_proxy.txt"

def thr_bing(
    data: tuple[object, list[dict]]
):
    processes = []
    func, data = data
    for d in data:
        mail = d.get('mail')
        proxy = d.get('proxy')
        t = tr.Thread(target=func, args=(mail, proxy))
        processes.append(t)
        t.start()
    
    for t in processes:
        t.join()


if __name__ == "__main__":

    mails = DB.get_emails()

    # while True:
    #     n += 1
    #     try:
    #         # cookies.append(load_cookies(f'./resources/cookies/cookies{n}.json'))
    #     except Exception as e:
    #         break
    
    proxies = proxy_from_file(proxy_file)

    mail_proxy = [{"mail": m, "proxy": p} for m, p in list(zip(mails, proxies))]
    # print(mail_proxy)

    data = (bing_loop, mail_proxy)

    thr_bing(data=data)
