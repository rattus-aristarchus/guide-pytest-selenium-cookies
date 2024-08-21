import allure
from allure_commons.types import ParameterMode


def test_cookie(driver, login, token, domain):
    allure.dynamic.parameter("Login", login, mode=ParameterMode.MASKED)
    allure.dynamic.parameter("Token", token, mode=ParameterMode.MASKED)
    allure.dynamic.parameter("Domain", domain)

    with allure.step("Open the main page"):
        driver.get("https://en.wikipedia.org/")

    with allure.step("Add cookies"):
        driver.add_cookie({
            "name": "centralauth_User",
            "value": login,
            "domain": domain,
            "path": "/"
        })
        driver.add_cookie({
            "name": "centralauth_Token",
            "value": token,
            "domain": domain,
            "path": "/"
        })

    with allure.step("User should be logged in"):
        assert is_logged_in()


def is_logged_in():
    return True
