import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/selects1.html'
try:
    options = webdriver.ChromeOptions()
    browser = webdriver.Remote('http://127.0.0.1:4444/wd/hub', options.to_capabilities())
    browser.get(link)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    sum = int(num1) + int(num2)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(sum))
    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
