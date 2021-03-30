import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
try:
    options = webdriver.ChromeOptions()
    browser = webdriver.Remote('http://127.0.0.1:4444/wd/hub', options.to_capabilities())
    browser.get(link)

    value_x = browser.find_element_by_id('treasure').get_attribute('valuex')
    value_calc = calc(value_x)
    browser.find_element_by_id('answer').send_keys(value_calc)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button.btn').click()
finally:
    time.sleep(10)
    browser.quit()
