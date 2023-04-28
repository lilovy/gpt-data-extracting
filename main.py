from src.tools.multi import multi_process, mlt, thr
from src.tools.extractor import combine, api_combine
from config import tokens, tok_prx, proxies, api_prx



n = 0

if __name__ == "__main__":
    # multi_process(combine, tok_prx, processes=len(tok_prx))
    # mlt(combine, tok_prx)
    # mlt(api_combine, api_prx)
    data = [(combine, tok_prx)]
    thr(data)
    # combine(tokens[n], proxies[n])