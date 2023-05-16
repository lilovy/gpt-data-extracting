from src.tools.multi import thr_bing
from src.tools.extractor import bing_loop
from src.tools.data_loader import load_cookies
from src.tools.proxy import proxy_from_file
from src.database.init_database import DB
import threading as tr


bing_proxy = "resources\proxies\\bing.txt"
login_proxy = "resources\proxies\\login.txt"


if __name__ == "__main__":

    mails = DB.get_emails()

    bing_p = proxy_from_file(bing_proxy)
    login_p = proxy_from_file(login_proxy)

    mail_proxy = [
        {
            "mail": m,
            "bing": b,
            "login": l,
        }
        for m, b, l in list(
            zip(
                mails,
                bing_p,
                login_p,
            )
        )
    ]

    # print(mail_proxy)

    # bing_loop(**mail_proxy[0])


    data = (bing_loop, mail_proxy)
    thr_bing(data=data)
