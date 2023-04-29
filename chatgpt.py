from src.tools.multi import thr
from src.tools.extractor import combine
from config import tokens, tok_prx, proxies


if __name__ == "__main__":

    data = [(combine, tok_prx)]
    thr(data)