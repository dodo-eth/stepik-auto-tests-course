import time

from browser import browser

link = 'http://suninjuly.github.io/registration1.html'

try:
    browser = browser()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('input[placeholder*="first name"]')
    input1.send_keys('Ivan')
    input2 = browser.find_element_by_css_selector('input[placeholder*="last name"]')
    input2.send_keys('Petrov')
    input3 = browser.find_element_by_css_selector('input[placeholder*="email"]')
    input3.send_keys('petrov@mail.ru')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
