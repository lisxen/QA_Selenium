import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationForms(unittest.TestCase):
    def test_link_1(self):
        link = "https://suninjuly.github.io/registration1.html"
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

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_link_2(self):
        link = "https://suninjuly.github.io/registration2.html"
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

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()
