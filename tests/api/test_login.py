import pytest
import allure

@allure.title("API-007 登录校验-正确账号")
@pytest.mark.api
def test_login_with_valid_details(api_client,test_user):
    response=api_client.post("/verifyLogin",data={"email":test_user["email"],"password":test_user["password"]})

    assert response.status_code == 200

    result=response.json()
    assert result["responseCode"] == 200
    assert "exists" in result.get("message","").lower()


@allure.title("API-008 登录校验-缺失参数")
@pytest.mark.api
def test_login_without_email(api_client):
    payload={
        "password":"Pass123"
    }
    response=api_client.post("/verifyLogin",data=payload)

    assert response.status_code == 200

    body=response.json()
    assert body.get("responseCode") == 400
    assert "missing" in body.get("message", "").lower(), "响应消息应包含参数缺失提示"
    assert "email" in body.get("message", "").lower(), "响应消息应提示email参数缺失"



@allure.title("API-009 登录校验-DELETE 方法不支持")
@pytest.mark.api
def test_delete_to_login(api_client):
    response=api_client.delete("/verifyLogin",data={})
    assert response.status_code == 200

    body=response.json()
    assert body["responseCode"] == 405
    assert "not supported" in body.get("message","").lower()

# @allure.title("API-010 登录校验-错误账号")
# @pytest.mark.api
# def test_login_with_invalid_details(api_client,test_user):
#     response=api_client.post("/verifyLogin",data={"email":test_user["email"],"password":"Pass123"})
#     assert response.status_code == 200
#     body=response.json()
#     assert body.get("responseCode") == 404
#     assert "not found" in body.get("message","").lower()
