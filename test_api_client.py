from core.api_client import ApiClient

def test_api_client_init():
    """测试 ApiClient 初始化"""
    api = ApiClient()
    assert api.base_url is not None
    print("客户端初始化成功")

def test_api_get_request():
    """测试 GET 请求"""
    api = ApiClient()
    res = api.get("productsList")
    assert res.status_code == 200
    print("GET 请求正常")

def test_api_post_request():
    """测试 POST 请求"""
    api = ApiClient()
    user = {
        "name": "test",
        "email": "test_unique_12345@qq.com",
        "password": "123456"
    }
    res = api.post("createAccount", data=user)
    assert res.status_code in [200, 201]
    print("POST 请求正常")