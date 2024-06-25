from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # заполнение списка выбранных элементов заданным параметром
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("Ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    # закрытие браузера
    browser.quit()
