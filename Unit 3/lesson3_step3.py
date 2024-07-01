import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Petrov")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email.send_keys("ivanpetrov@xxxx.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1")))
        welcome_text = welcome_text_elt.text
        return welcome_text
    except:
        browser.quit()

def test_link_1():
    link = "https://suninjuly.github.io/registration1.html"
    assert test_registration(link) == "Congratulations! You have successfully registered!", "Error"

def test_link_2():
    link = "https://suninjuly.github.io/registration2.html"
    assert test_registration(link) == "Congratulations! You have successfully registered!", "Error"

if __name__ == "__main__":
    pytest.main()
