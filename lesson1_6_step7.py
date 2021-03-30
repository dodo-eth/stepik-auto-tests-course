import time
import math

from browser import browser

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = browser()
    browser.get(link)

    elements = browser.find_elements_by_css_selector('input[type=text]')
    for element in elements:
        element.send_keys('Ok')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
