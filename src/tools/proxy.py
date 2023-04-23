from lxml import html
import requests


proxy_url = 'https://free-proxy-list.net/'

ip = "//*[@id='list']/div/div[2]/div/table/tbody/tr[*]/td[1]/text()"

port = "//*[@id='list']/div/div[2]/div/table/tbody/tr[*]/td[2]/text()"

protocol = "//*[@id='list']/div/div[2]/div/table/tbody/tr[*]/td[7]/text()"


def proxy_list(
    url: str = proxy_url,
    ip: str = ip,
    port: str = port,
    protocol: str = protocol,
    ) -> list[tuple[str, str]]:

    resp = requests.get(url)
    tree = html.fromstring(resp.content)

    ip = tree.xpath(ip)
    port = tree.xpath(port)
    protocol = tree.xpath(protocol)

    proxy = [{"protocol": 'https' if protocol[n] == 'yes' else 'http', "proxy": f'{i}:{port[n]}'} for n, i in enumerate(ip)]
    
    return proxy


if __name__ == "__main__":
    print(proxy_list())
