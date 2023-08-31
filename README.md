># ДИПЛОМНЫЙ ПРОЕКТ ПО АВТОМАТИЗАЦИИ ТЕСТИРОВАНИЯ SKILLFACTORY QAP-1035 

## Необходимо протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком.

→ Объект тестирования: https://b2c.passport.rt.ru

→ [Требования по проекту (.doc)](https://docs.google.com/document/d/1WTvxg7w3UNJYGsjplyZFLNdh7lWv9J3P/edit?usp=sharing&ouid=114718040835219983979&rtpof=true&sd=true)




## Задание заказчика:

1. Протестировать требования.
2. Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
3. Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
4. Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)

## Ожидаемый результат

1. Перечислены инструменты, которые применялись для тестирования.

   * Почему именно этот инструмент и эту технику.
   * Что им проверялось.
   * Что именно в нем сделано.
   
2. К выполненному заданию прикреплены:

   * Набор тест-кейсов;
   * Набор автотестов на GitHub.
   * Описание оформленных дефектов.

***
### **В корневом каталоге проекта содержаться:**
* [conftest.py](https://github.com/Ioganus/Final_Project/blob/master/conftest.py) - содержит условия для выполнения тестов.
* [pytest.ini](https://github.com/Ioganus/Final_Project/blob/master/pytest.ini) - содержит указание на автоматическую генерацию html-отчета.
* [requirements.txt](https://github.com/Ioganus/Final_Project/blob/master/requirements.txt) - содержит все библиотеки и зависимости проекта.
***
### **Директория pages содержит:**
* [base_page.py](https://github.com/Ioganus/Final_Project/blob/master/pages/base_page.py) - содержит все общие методы и утилиты для всех страниц.
* [auth_page.py](https://github.com/Ioganus/Final_Project/blob/master/pages/auth_page.py) - содержит специфичные методы и утилиты для страницы авторизации.
***
### **Директория tests содержит:**
* [assets](https://github.com/Ioganus/Final_Project/blob/master/tests/assets/style.css) - содержит CSS-стили для html-отчёта.
* [base_test.py](https://github.com/Ioganus/Final_Project/blob/master/tests/base_test.py) - содержит базовый тестовый класс.
* [test_auth.py](https://github.com/Ioganus/Final_Project/blob/master/tests/test_auth.py) - содержит автотесты для страницы авторизации.
***
### **Директория utilities содержит:**
* [locators.py](https://github.com/Ioganus/Final_Project/blob/master/utilities/locators.py) - содержит локаторы страницы.
* [test_data.py](https://github.com/Ioganus/Final_Project/blob/master/utilities/test_data.py) - содержит все данные для проверок авторизации.
***

→ [Тест-кейсы (.excel)](https://docs.google.com/spreadsheets/d/1mKrAn4WIsXX9F3Wf-xA8SbYxvXsu38-zzBfTzodhNXc/edit?usp=sharing)

→ [Баг-репорты (.excel)](https://docs.google.com/spreadsheets/d/1K00tMRM30VDBTPKJIWvsLRmD6Xxsd4bREQtj_u9mFBc/edit?usp=sharing)

### При разработке тест-кейсов были применены следующие техники тест-дизайна: 
 
* эквивалентное разбиение
* анализ граничных значений
* предугадывание ошибок
* [диаграмма перехода состояния (.png)](https://drive.google.com/file/d/1wmqN3gR95k3_4ULrMrLiK4frsXaxL-Pf/view?usp=sharing)


### Инструменты, которые применялись для тестирования.

* Для тестирования сайта был использован 
интсрумент [Selenium](https://www.selenium.dev/).
* Специальный тестовый фреймворк [Pytest](https://docs.pytest.org/).
* Плагин для pytest, который генерирует HTML-отчет по результатам тестов [pytest-html](https://pytest-html.readthedocs.io/en/latest/).
* Опционально можете установить плагин [allure-pytest](https://pypi.org/project/allure-pytest/) и скачать для неё [командную строку](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/) для генерации красивых html-отчётов.
* Для определения локаторов использовались 
следующие инструменты: [DevTools](https://developer.chrome.com/docs/devto), [ChroPath](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo).

### Запуск тестов:
* установить все библиотеки и зависимости: `pip install -r requirements.txt`.
* убедитесь что у вас присутствуют основные браузеры для тестирования - в файле conftest.py у фикстуры initialize_driver можете изменить браузер.
* запустить тесты: `pytest tests/test_auth.py`.
* запустить один тест: `pytest tests/test_auth.py::TestAuth::название_нужного_теста`.


Была добавлена фикстура для пропуска тестов если на странице возникает капча. Рекомендуется запускать не более 2-3 тестов, связанных с авторизацией, чтобы избежать её возникновение.

