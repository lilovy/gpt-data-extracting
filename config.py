from dotenv import load_dotenv, find_dotenv
from os import getenv
from src.tools.proxy import proxy_from_file

load_dotenv(find_dotenv())


token1 = getenv('token1')
token2 = getenv('token2')
api_token1 = getenv('api_token1')
api_token2 = getenv('api_token2')

tokens = [
    token1,
    token2,
]

api_tokens = [
    api_token1,
    api_token2,
]

proxy_file = 'resources\proxies\\bing.txt'
proxies = proxy_from_file(proxy_file)

tok_prx = list(zip(tokens, proxies))

api_prx = list(zip(api_tokens, proxies))

base_proxy_dir = "resources/proxies/credential/"