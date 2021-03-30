import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    options = webdriver.ChromeOptions()
    browser = webdriver.Remote('http://127.0.0.1:4444/wd/hub', options.to_capabilities())
    browser.get(link)

    WebDriverWait(browser, 15).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element_by_id('book').click()

    value_x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(value_x))
    button_submit = browser.find_element_by_id('solve')
    browser.execute_script('arguments[0].scrollIntoView();', button_submit)
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
