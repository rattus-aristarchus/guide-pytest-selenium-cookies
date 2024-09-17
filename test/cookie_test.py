import json

from selenium.webdriver.common.by import By


def test_cookie(driver, login, password, domain):
    driver.get("https://www.saucedemo.com/")
    driver.add_cookie({
        "name": "session-username",
        "value": login,
        "domain": domain,
        "path": "/"
    })
    driver.add_cookie({
        "name": "standard_user",
        "value": password,
        "domain": domain,
        "path": "/"
    })
    driver.get("https://www.saucedemo.com/")
    driver.refresh()

    assert is_logged_in(driver)


def test_login(driver):

    driver.get("https://www.saucedemo.com/")
    log_in(driver)

    assert is_logged_in(driver)


def log_in(driver):
    input_username = driver.find_element(By.ID, "user-name")
    input_username.send_keys("standard_user")
    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()


def is_logged_in(driver):
    return driver.current_url == "https://www.saucedemo.com/inventory.html"
    # $("[data-test='secondary-header']").shouldBe(Condition.visible);


def test_get_cookies(driver):
    driver.get("https://www.saucedemo.com/")
    log_in(driver)
    cookies = driver.get_cookies()
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)


def test_load_cookies(driver):
    driver.get("https://www.saucedemo.com/")
    with open('cookies.json', 'r') as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.refresh()

    assert is_logged_in(driver)
