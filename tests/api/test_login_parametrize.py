import pytest
import allure


@pytest.mark.parametrize(
    "payload, expected_code, expected_msg_keyword",
    [
        ({"password": "Pass123"}, 400, "email"),
        ({"email": "any@example.com"}, 400, "password"),
        ({"email": "nonexist@example.com", "password": "Pass123"}, 404, "not found"),
        ({"email": "", "password": ""}, 400, "email"),
    ]
)
@allure.title("登录异常场景测试")
def test_login_exception_scenarios(api_client, payload, expected_code, expected_msg_keyword):
    response = api_client.post("/verifyLogin", data=payload)
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == expected_code
    assert expected_msg_keyword in body.get("message", "").lower()



@allure.title("正确账号登录成功")
def test_login_success(api_client, test_user):
    response = api_client.post("/verifyLogin", data={
        "email": test_user["email"],
        "password": test_user["password"]
    })
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == 200
    assert "exists" in body.get("message", "").lower()