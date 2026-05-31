import pytest
import allure

@allure.title("API-001 产品列表查询")
@pytest.mark.api
def test_get_products_list(api_client):
    response=api_client.get("/productsList")
    assert response.status_code == 200
    body=response.json()

    assert body.get("responseCode") == 200
    assert isinstance(body.get("products"),list)

@allure.title("API-002 POST 产品列表接口不支持")
@pytest.mark.api
def test_products_list_not_supported(api_client):
    response=api_client.post("/productsList")
    assert response.status_code == 200
    body = response.json()
    print(body)
    assert body.get("responseCode") == 405
    assert "not supported" in body.get("message","").lower()