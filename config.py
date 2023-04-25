from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())


token1 = getenv('token1')
token2 = getenv('token2')
api_token = getenv('api_token')

tokens = [
    token1,
    token2,
]