import pytest

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

