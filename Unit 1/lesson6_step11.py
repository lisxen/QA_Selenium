from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # ссылка без багов, допускающая применение НЕуникальных селекторов
    # link = "http://suninjuly.github.io/registration1.html"

    # ссылка с багом, выдающая NoSuchElementException при уникальных селекторах
    link = "https://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # заполнение обязательных полей
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("ivanpetrov@xxxx.com")

    # просмотр заполненных полей
    time.sleep(1)

    # отправка заполненной формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # проверка регистрации, ожидание загрузки страницы
    time.sleep(1)

    # поиск элемента, содержащего текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # запись в переменную welcome_text текста из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # проверка, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    # закрытие браузера
    browser.quit()
