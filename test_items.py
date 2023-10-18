from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_the_presence_of_a_button(browser):
    try:
        assert browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form").is_displayed()    # (is_displayed(): Этот метод проверяет, присутствует ли элемент на странице и виден ли он пользователю. Он возвращает значение True, если элемент отображается, и False, если он не отображается.)
        print("Элемент найден")
    except NoSuchElementException:                                                            # чтобы исключение работало его импортируем выше from selenium.common import NoSuchElementException
        print("Элемент не найден")

# так же эту задачу можно решить с помощью find_elements, пример ниже (проверка, что список больше нуля)
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.example.com")
# elements = driver.find_elements_by_xpath("//input[@name='username']")
# assert len(elements) > 0, "Элемент отсутствует на странице"
# print("Элемент присутствует на странице")
