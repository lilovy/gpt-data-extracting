import json
import uuid


class ProxyBuilder(object):

    __schema = {
        "proxy_builder": {
            "type": 1,
            "color": "#66cc66",
            "title": "proxy_builder",
            "active": True,
            "address": "",
            "port": 0,
            "proxyDNS": False,
            "username": "",
            "password": "",
            "whitePatterns": [
                {
                    "title": "all URLs",
                    "pattern": "*",
                    "type": 1,
                    "protocols": 1,
                    "active": False
                },
                {
                    "title": "bing.com",
                    "pattern": "*",
                    "type": 1,
                    "protocols": 1,
                    "active": True
                }
            ],
            "blackPatterns": [],
            "pacURL": "",
            "index": 9007199254740990
        },
        "logging": {
            "size": 100,
            "active": False
        },
        "mode": "patterns",
        "browserVersion": "112.0.2",
        "foxyProxyVersion": "7.5.1",
        "foxyProxyEdition": "standard"
        }

    def __init__(self, address: str, port: int, username: str = "", password: str = ""):
        self.address = address
        self.port = port
        self.username = username
        self.password = password
        self.schema = self.__build_schema()

    def __build_schema(self):
        self._schema = self.__schema
        self._schema['proxy_builder']['title'] = f"{self.address}:{self.port}"
        self._schema['proxy_builder']['address'] = self.address
        self._schema['proxy_builder']['port'] = self.port
        self._schema['proxy_builder']['username'] = self.username
        self._schema['proxy_builder']['password'] = self.password
        
        return self._schema

    def get(self):
        return json.dumps(self.schema)

    def export(self, filedir: str):
        with open(f'{filedir}/{self.address}-{self.port}.json', 'w') as f:
            json.dump(self._schema, f, indent=2)
