import json
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture
def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


url_list = [
    "236895",
    "236896",
    "236897",
    "236898",
    "236899",
    "236903",
    "236904",
    "236905"
]


class TestParametrization():

    @pytest.mark.parametrize('url', url_list)
    def test_authorisation(self, browser, url, load_config):
        link = f"https://stepik.org/lesson/{url}/step/1"
        browser.get(link)
        btn_login = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'navbar__auth_login')))
        btn_login.click()

        # авторизация
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        browser.find_element(By.ID, 'id_login_email').send_keys(login)
        browser.find_element(By.ID, 'id_login_password').send_keys(password)
        browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader').click()
        WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__profile-img")))

        # ввод ответа
        text_area = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.ember-text-area')))
        text_area.clear()
        text_area.send_keys(str(math.log(int(time.time()))))
        btn_submit = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
        btn_submit.click()

        # получение сообщения
        message = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.smart-hints.ember-view > p')))
        assert message.text == 'Correct!', message.text
