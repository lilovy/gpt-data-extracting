from src.tools import multi_process
from src.tools import combine
from config import tokens

if __name__ == "__main__":
    multi_process(combine, tokens)