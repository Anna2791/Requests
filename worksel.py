# Напишите программу, с помощью которой можно искать информацию на Википедии
# с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
#     -листать параграфы текущей статьи;
#     перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# -   листать параграфы статьи;
# - перейти на одну из внутренних статей.
#    выйти из программы.
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запуск браузера
browser = webdriver.Firefox()

# Переход на главную страницу Википедии
browser.get('https://ru.wikipedia.org/wiki/Заглавная_страница')

# Поиск поля ввода и отправка запроса
search_box = browser.find_element(By.ID, 'searchInput')
user_input = input('Введите интересующую вас тему: ')
search_box.send_keys(user_input)
search_box.send_keys(Keys.RETURN)
time.sleep(3)
click = browser.find_element(By.LINK_TEXT, user_input)
click.click()
time.sleep(2)
# Функция для просмотра параграфов
def scroll_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input("Нажмите Enter для продолжения...")

# Основной цикл программы
while True:
    user_choice = int(input('Выберите действие:\n1 - Листать параграфы текущей статьи;\n2 - Перейти на одну из связанных страниц;\n3 - Закончить поиск и закрыть: '))

    if user_choice == 1:
        scroll_paragraphs()

    elif user_choice == 2:
        links = browser.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
        for index, link in enumerate(links):
            if link.text:
                print(f"{index}: {link.text}")
        link_choice = int(input("Введите номер ссылки, чтобы перейти: "))
        links[link_choice].click()
        time.sleep(3)

    elif user_choice == 3:
        print('Поиск завершен')
        break

    else:
        print("Неверный выбор. Попробуйте еще раз.")

# Закрытие браузера
browser.quit()