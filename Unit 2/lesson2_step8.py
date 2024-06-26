from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Enter first name']")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Enter last name']")
    last_name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Enter email']")
    email.send_keys("ivanpetrov@xxxx.com")

    # загрузка файла из текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "lesson2_step8.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()
