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



@pytest.fixture(scope="function")
def test_user(api_client):
    payload = user_payload()
    api_client.post("/createAccount",data=payload)
    yield payload
    api_client.delete(endpoint="/deleteAccount",
                      data={"email":payload["email"],"password":payload["password"]},)



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


#
# @pytest.fixture(scope="function")
# def test_user(api_client):
#     payload = user_payload()
#     api_client.post("/createAccount", data=payload)
#     yield payload
#     api_client.delete("/deleteAccount", data={"email": payload["email"], "password": payload["password"]})
#

