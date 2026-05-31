import pytest
from playwright.sync_api import sync_playwright

from core.api_client import ApiClient
from utils.config import load_config
from utils.data_factory import user_payload


@pytest.fixture(scope="session")
def config() -> dict:
    return load_config()


@pytest.fixture(scope="session")
def api_client(config:dict):
    return ApiClient()


@pytest.fixture(scope="session")
def test_user(api_client):
    payload = user_payload()
    api_client.post("/createAccount",data=payload)
    return payload









@pytest.fixture(scope="session")
def ui_base_url(config:dict) -> str:
    return config["ui_base_url"].rstrip("/")

@pytest.fixture(scope="session")
def browser(config):
    headless = config.get("headless", True)
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            slow_mo=200
        )
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.fixture
def ui_user(config):
    payload = user_payload()
    api_client = ApiClient()
    response = api_client.post("/createAccount", data=payload)
    assert response.status_code == 200, f"创建用户失败: {response.text}"
    yield payload
    api_client.delete(
        endpoint="/deleteAccount",
        data={"email": payload["email"], "password": payload["password"]},
    )
