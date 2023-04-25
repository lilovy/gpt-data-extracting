from src.tools.multi import multi_process, mlt
from src.tools.extractor import combine
from config import tokens, tok_prx, proxies



n = 0

if __name__ == "__main__":
    # multi_process(combine, tok_prx, processes=len(tok_prx))
    mlt(combine, tok_prx)
    # combine(tokens[n], proxies[n])