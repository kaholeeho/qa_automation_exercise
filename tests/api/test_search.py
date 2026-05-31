import pytest
import allure

@allure.title("API-005 搜索产品-正常关键词")
@pytest.mark.api
def test_search_product_normal(api_client):
    response=api_client.post("/searchProduct",data={"search_product":"tshirt"})
    assert response.status_code ==200
    body= response.json()
    assert body.get("responseCode") == 200
    assert isinstance(body.get("products"),list)
    assert body.get("products")

@allure.title("API-005-2 搜索产品-特殊字符")
@pytest.mark.api
def test_search_special_characters(api_client):
    response = api_client.post("/searchProduct", data={"search_product": "@@@###"})
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == 200
    assert isinstance(body.get("products"), list)

@allure.title("API-006 搜索产品-缺失参数")
@pytest.mark.api
def test_search_missing_param(api_client):
    response = api_client.post("/searchProduct")
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == 400
    assert "search_product parameter" in body.get("message","").lower()
    assert "missing" in body.get("message","").lower()