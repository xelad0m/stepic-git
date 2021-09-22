from selenium import webdriver
from selenium.webdriver.common.by import By

import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(link1)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'first_class')]/input")
    second_name = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'second_class')]/input")
    email = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'third_class')]/input")
    required = [first_name, second_name, email]

    phone = browser.find_element(By.XPATH, "//div[@class='second_block']/div[contains(@class, 'first_class')]/input")
    address = browser.find_element(By.XPATH, "//div[@class='second_block']/div[contains(@class, 'second_class')]/input")
    optional = [phone, address]

    for element in required + optional:
        element.send_keys("Some text")

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

    time.sleep(3)