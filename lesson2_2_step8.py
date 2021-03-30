import os
import time

from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'
try:
    options = webdriver.ChromeOptions()
    browser = webdriver.Remote('http://127.0.0.1:4444/wd/hub', options.to_capabilities())
    browser.get(link)

    browser.find_element_by_name('firstname').send_keys('Ivan')
    browser.find_element_by_name('lastname').send_keys('Petrov')
    browser.find_element_by_name('email').send_keys('petrov@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element_by_id('file').send_keys(file_path)

    browser.find_element_by_css_selector('button.btn').click()


finally:
    time.sleep(10)
    browser.quit()
