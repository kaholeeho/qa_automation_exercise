import random
import string
from datetime import datetime,timezone


def unique_email(prefix : str = "autotest") -> str :
    timestamp=datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    suffix="".join(random.choices(string.ascii_lowercase + string.digits,k = 6))
    return f"{prefix}_{timestamp}_{suffix}@example.com"

# 自己扩展 登录请求体、产品请求体……
def login_payload():
    pass
def product_payload():
    pass


def user_payload(email : str | None = None,password : str = "Pass1234!") -> dict:
    email_value = email or unique_email()
    return {
        "name":"Codex User",
        "email":email_value,
        "password":password,
        "title":"Mr",
        "birth_date": "10",
        "birth_month": "May",
        "birth_year": "1990",
        "firstname": "Codex",
        "lastname": "User",
        "company": "Codex Inc",
        "address1": "123 Test St",
        "address2": "Apt 1",
        "country": "United States",
        "zipcode": "10001",
        "state": "NY",
        "city": "New York",
        "mobile_number": "1234567890",
    }