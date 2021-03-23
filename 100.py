from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 16).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x_L = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x_L)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    btn = browser.find_element_by_css_selector("#solve")
    btn.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

