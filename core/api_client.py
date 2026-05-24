import requests
from utils.config import load_config

class ApiClient:

    def __init__(self):
        # 从配置文件自动读取 base_url
        self.config = load_config()
        self.base_url = self.config["api_base_url"]
        self.timeout = self.config["timeout_seconds"]
        self.session = requests.Session()


    def request(
            self,
            method : str,
            endpoint,
            params : dict | None = None,
            data : dict | None = None,
            json:dict |None=None,
            headers : dict | None = None
    ) -> requests.Response:
        #通用请求方法
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            json=json,
            headers=headers,
            timeout=self.timeout
        )
        return response

    def get(self,endpoint : str,params : dict | None = None,headers: dict | None = None):
        return self.request("GET",endpoint,params = params,headers=headers)
                              #关键字传参，request函数能对应接收参数，参数能准确传递

    def post(self,endpoint : str,data : dict | None = None,json: dict | None = None,headers: dict | None = None):
        return self.request("POST",endpoint,data=data,json=json,headers=headers)

    def put(self,endpoint : str,data : dict | None = None,json: dict | None = None,headers: dict | None = None):
        return self.request("PUT",endpoint,data=data,json=json,headers=headers)

    def delete(self,endpoint : str,data : dict | None = None,headers: dict | None = None):
        return self.request("DELETE",endpoint,data=data,headers=headers)
