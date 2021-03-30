import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'
try:
    options = webdriver.ChromeOptions()
    browser = webdriver.Remote('http://127.0.0.1:4444/wd/hub', options.to_capabilities())
    browser.get(link)

    browser.find_element_by_css_selector('button.btn').click()
    browser.switch_to.alert.accept()
    value_x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(value_x))
    browser.find_element_by_css_selector('button.btn').click()
finally:
    time.sleep(10)
    browser.quit()
