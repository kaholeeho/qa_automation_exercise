import pytest
import allure


@allure.title("API-003 品牌列表查询")
@pytest.mark.api
def test_get_brands_list(api_client):
    response=api_client.get("/brandsList")
    assert response.status_code == 200
    body=response.json()
    assert body.get("responseCode") == 200
    assert isinstance(body.get("brands"),list)


@allure.title("API-004 PUT 品牌列表接口不支持")
@pytest.mark.api
def test_brands_list_not_supported(api_client):
    response = api_client.put("/brandsList")
    assert response.status_code == 200
    body = response.json()
    assert body.get("responseCode") == 405
    assert "not supported" in body.get("message","").lower()