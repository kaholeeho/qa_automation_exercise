import pytest

from tests.conftest import api_client
from utils.data_factory import user_payload

"API-011 创建账户"
@pytest.mark.api
# pytest fixture 的依赖注入机制
def test_create_account(api_client):
    payload=user_payload()
    response = api_client.post("/createAccount",data=payload)
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == 201
    assert "created" in body.get("message","").lower()


"API-014 获取用户信息"
@pytest.mark.api
def test_get_user_detail(api_client,test_user):
        user_email = test_user["email"]
        response = api_client.get(
            "/getUserDetailByEmail",
            params={"email": user_email}
        )
        # 1. 状态码断言
        assert response.status_code == 200
        # 2. 获取返回数据
        result = response.json()
        # 3. 业务断言（正确写法！）
        assert result["responseCode"] == 200
        assert result["user"]["email"] == user_email
        assert result["user"]["name"] == test_user["name"]


"API-013 更新账户信息"
@pytest.mark.api
def test_update_account(api_client, test_user):
    # 准备更新数据
    new_name = "UPDATED_NAME"
    update_data = {
        "name": new_name,
        "email": test_user["email"],
        "password": test_user["password"],  # 必须用原来的密码！
    }

    login_resp = api_client.post(
        "/verifyLogin",
        data={"email": test_user["email"], "password": test_user["password"]}
    )
    assert login_resp.status_code == 200, "登录请求失败"

    resp = api_client.put("/updateAccount", data=update_data)
    print("更新响应:", resp.json())

    assert resp.status_code == 200, "更新用户请求失败，状态码非200"
    body = resp.json()
    assert body["responseCode"] == 200, "更新用户业务状态码非200"
    assert "updated" in body["message"].lower(), "响应消息不符合预期"

    get_resp = api_client.get("/getUserDetailByEmail", params={"email": test_user["email"]})
    user = get_resp.json()["user"]
    assert user["name"] == new_name, "用户名称未更新成功"


"API-007 使用有效详细信息登录"
@pytest.mark.api
def test_login_with_valid_details(api_client,test_user):
    response=api_client.post("/verifyLogin",data={"email":test_user["email"],"password":test_user["password"]})

    assert response.status_code == 200

    result=response.json()
    assert result["responseCode"] == 200
    assert "exists" in result.get("message","").lower()
