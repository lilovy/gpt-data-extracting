from src.tools.multi import multi_process
from src.tools.extractor import combine
from config import tokens

if __name__ == "__main__":
    multi_process(combine, tokens)