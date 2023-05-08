from src.tools.multi import thr_bing
from src.tools.extractor import bing_loop
from src.tools.data_loader import load_cookies
from src.tools.proxy import proxy_from_file
from src.database.init_database import DB
import threading as tr


proxy_file = "resources\proxies\\bing_proxy.txt"


if __name__ == "__main__":

    mails = DB.get_emails()

    proxies = proxy_from_file(proxy_file)

    mail_proxy = [{"mail": m, "proxy": p} for m, p in list(zip(mails, proxies))]
    
    print(mail_proxy)

    data = (bing_loop, mail_proxy)

    # thr_bing(data=data)
